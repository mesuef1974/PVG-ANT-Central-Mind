d <- read.csv("../data/pvg_lpd_dataset_001.csv", check.names = FALSE)
research <- subset(d, role == "research")
train <- subset(research, analysis_split == "train")
test <- subset(research, analysis_split == "test")
target <- "li_std_residual"
classical <- c("log_x", "log_h", "theta_empirical")
vsds <- grep("^(r_d_|vsds_|sift_residual_|sift_ratio_)", names(d), value = TRUE)
rmse <- function(y, p) sqrt(mean((y - p)^2))
mae <- function(y, p) mean(abs(y - p))
r2 <- function(y, p) 1 - sum((y - p)^2) / sum((y - mean(y))^2)
fit_model <- function(features) {
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