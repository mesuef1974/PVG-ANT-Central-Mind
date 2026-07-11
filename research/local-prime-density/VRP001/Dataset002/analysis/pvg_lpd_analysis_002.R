data_path <- "../data/pvg_lpd_dataset_002.csv"
if (!file.exists(data_path)) {
  stop("Dataset 002 is missing. Run build_dataset_002.py before this analysis.")
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
lagLambda <- grep("^pre_lambda_(density|residual_per_sqrt)", names(d), value = TRUE)
chars <- grep("^pre_(chi|character_energy)", names(d), value = TRUE)
residue <- grep("^pre_residue_(energy|max)", names(d), value = TRUE)
vsds <- grep("^(r_d_|vsds_|sift_residual_|sift_ratio_)", names(d), value = TRUE)

feature_groups <- list(
  lagLambda = lagLambda,
  characters = chars,
  residue = residue,
  vsds = vsds
)
for (nm in names(feature_groups)) {
  if (length(feature_groups[[nm]]) == 0) stop(paste("Empty feature group:", nm))
}

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

sets <- list(
  "Classical LM" = classical,
  "Classical + lagged Lambda" = c(classical, lagLambda),
  "Classical + Lambda + characters" = c(classical, lagLambda, chars),
  "Classical + Lambda + characters + residue energy" = c(classical, lagLambda, chars, residue),
  "Full past-only + current VSDS" = c(classical, lagLambda, chars, residue, vsds)
)

models <- lapply(sets, fit_model)
predictions <- lapply(models, predict, newdata = test)
comparison <- data.frame(
  model = names(sets),
  rmse = vapply(predictions, function(p) rmse(test[[target]], p), numeric(1)),
  mae = vapply(predictions, function(p) mae(test[[target]], p), numeric(1)),
  r2 = vapply(predictions, function(p) r2(test[[target]], p), numeric(1))
)
print(comparison)

set.seed(20260711)
B <- 5000
classical_pred <- predictions[["Classical LM"]]
candidate_names <- setdiff(names(predictions), "Classical LM")
bootstrap <- data.frame()
for (nm in candidate_names) {
  candidate_pred <- predictions[[nm]]
  delta <- numeric(B)
  for (b in seq_len(B)) {
    idx <- sample(seq_len(nrow(test)), replace = TRUE)
    delta[b] <- rmse(test[[target]][idx], classical_pred[idx]) -
      rmse(test[[target]][idx], candidate_pred[idx])
  }
  probability_better <- mean(delta > 0)
  p_one_sided <- 1 - probability_better
  bootstrap <- rbind(
    bootstrap,
    data.frame(
      model = nm,
      improvement_vs_classical = rmse(test[[target]], classical_pred) - rmse(test[[target]], candidate_pred),
      bootstrap_ci_lower = unname(quantile(delta, 0.025)),
      bootstrap_median = unname(quantile(delta, 0.5)),
      bootstrap_ci_upper = unname(quantile(delta, 0.975)),
      probability_better = probability_better,
      p_one_sided = p_one_sided,
      p_bonferroni = min(1, p_one_sided * length(candidate_names))
    )
  )
}
print(bootstrap)

primary <- subset(bootstrap, model == "Classical + lagged Lambda")
exploratory <- subset(
  bootstrap,
  model == "Classical + Lambda + characters + residue energy"
)

primary_pass <- nrow(primary) == 1 &&
  primary$improvement_vs_classical > 0 &&
  primary$bootstrap_ci_lower > 0 &&
  primary$probability_better >= 0.95

exploratory_unadjusted_pass <- nrow(exploratory) == 1 &&
  exploratory$improvement_vs_classical > 0 &&
  exploratory$bootstrap_ci_lower > 0 &&
  exploratory$probability_better >= 0.95

exploratory_adjusted_pass <- exploratory_unadjusted_pass &&
  exploratory$p_bonferroni < 0.05

cat("Primary model pass:", primary_pass, "\n")
cat("Exploratory model unadjusted pass:", exploratory_unadjusted_pass, "\n")
cat("Exploratory model multiplicity-adjusted pass:", exploratory_adjusted_pass, "\n")

write.csv(comparison, "../data/r_model_comparison_002.csv", row.names = FALSE)
write.csv(bootstrap, "../data/r_bootstrap_002.csv", row.names = FALSE)
