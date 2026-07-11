data_path <- "../data/pvg_lpd_dataset_001.csv"
if (!file.exists(data_path)) {
  stop("Dataset 001 is missing. Run build_dataset_001.py before this analysis.")
}

d <- read.csv(data_path, check.names = FALSE)
required <- c(
  "role", "analysis_split", "li_std_residual",
  "log_x", "log_h", "theta_empirical"
)
missing_required <- setdiff(required, names(d))
if (length(missing_required) > 0) {
  stop(paste("Missing required columns:", paste(missing_required, collapse = ", ")))
}

research <- subset(d, role == "research")
train <- subset(research, analysis_split == "train")
test <- subset(research, analysis_split == "test")
if (nrow(train) == 0 || nrow(test) == 0) stop("Train/test split is empty")

target <- "li_std_residual"
classical <- c("log_x", "log_h", "theta_empirical")
vsds <- grep("^(r_d_|vsds_|sift_residual_|sift_ratio_)", names(d), value = TRUE)
if (length(vsds) == 0) stop("No VSDS features found in the dataset")

validate_pair <- function(y, p) {
  if (length(y) != length(p)) stop("Metric vectors have different lengths")
  if (length(y) == 0) stop("Metric vectors are empty")
  if (any(!is.finite(y)) || any(!is.finite(p))) stop("Metric vectors contain NA/Inf")
}
rmse <- function(y, p) {
  validate_pair(y, p)
  sqrt(mean((y - p)^2))
}
mae <- function(y, p) {
  validate_pair(y, p)
  mean(abs(y - p))
}
r2 <- function(y, p) {
  validate_pair(y, p)
  denom <- sum((y - mean(y))^2)
  if (denom == 0) stop("R-squared denominator is zero")
  1 - sum((y - p)^2) / denom
}

fit_model <- function(features) {
  if (length(features) == 0) stop("Cannot fit a model with no features")
  missing_features <- setdiff(features, names(train))
  if (length(missing_features) > 0) {
    stop(paste("Missing model features:", paste(missing_features, collapse = ", ")))
  }
  f <- as.formula(paste(target, "~", paste(features, collapse = " + ")))
  lm(f, data = train)
}

m_classical <- fit_model(classical)
m_full <- fit_model(c(classical, vsds))
p0 <- rep(0, nrow(test))
pc <- predict(m_classical, newdata = test)
pf <- predict(m_full, newdata = test)

result <- data.frame(
  model = c("Li baseline", "Classical LM", "Classical + VSDS LM"),
  rmse = c(rmse(test[[target]], p0), rmse(test[[target]], pc), rmse(test[[target]], pf)),
  mae = c(mae(test[[target]], p0), mae(test[[target]], pc), mae(test[[target]], pf)),
  r2 = c(r2(test[[target]], p0), r2(test[[target]], pc), r2(test[[target]], pf))
)
print(result)

set.seed(20260711)
B <- 5000
delta <- numeric(B)
for (b in seq_len(B)) {
  idx <- sample(seq_len(nrow(test)), replace = TRUE)
  delta[b] <- rmse(test[[target]][idx], pc[idx]) - rmse(test[[target]][idx], pf[idx])
}
print(quantile(delta, c(0.025, 0.5, 0.975)))
print(mean(delta > 0))
