args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) != 1) stop("Cannot resolve R script path")
script_path <- normalizePath(sub("^--file=", "", file_arg), mustWork = TRUE)
script_dir <- dirname(script_path)
root <- dirname(script_dir)
local_prime_density <- normalizePath(file.path(root, "..", ".."), mustWork = TRUE)

train_path <- file.path(
  local_prime_density,
  "VRP001", "Dataset002", "data", "pvg_lpd_dataset_002.csv"
)
test_path <- file.path(root, "data", "pvg_lpd_dataset_003.csv")
output_dir <- file.path(root, "data")

if (!file.exists(train_path)) stop("Dataset 002 training file is missing")
if (!file.exists(test_path)) stop("Dataset 003 test file is missing")

source <- read.csv(train_path, check.names = FALSE)
test <- read.csv(test_path, check.names = FALSE)
training <- subset(
  source,
  role == "research" & analysis_split %in% c("train", "validation")
)
if (nrow(training) != 535) stop("Unexpected frozen training row count")
if (nrow(test) != 480) stop("Unexpected Dataset 003 row count")

target <- "li_std_residual"
classical <- c("log_x", "log_h", "theta_empirical")
lagged_lambda <- grep(
  "^pre_lambda_(density|residual_per_sqrt)",
  names(source),
  value = TRUE
)
characters <- grep(
  "^pre_(chi|character_energy)",
  names(source),
  value = TRUE
)
residue <- grep(
  "^pre_residue_(energy|max)",
  names(source),
  value = TRUE
)

if (length(classical) != 3) stop("Classical feature count changed")
if (length(lagged_lambda) != 6) stop("Lagged-Lambda feature count changed")
if (length(characters) != 21) stop("Character feature count changed")
if (length(residue) != 36) stop("Residue feature count changed")

candidate <- c(classical, lagged_lambda, characters, residue)
secondary <- c(classical, lagged_lambda)
if (length(candidate) != 66) stop("Primary feature count changed")
missing_test <- setdiff(candidate, names(test))
if (length(missing_test) > 0) {
  stop(paste("Dataset 003 lacks frozen features:", paste(missing_test, collapse = ", ")))
}

validate_pair <- function(y, prediction) {
  if (length(y) != length(prediction)) stop("Metric vector lengths differ")
  if (length(y) == 0) stop("Metric vectors are empty")
  if (any(!is.finite(y)) || any(!is.finite(prediction))) {
    stop("Metric vectors contain NA or Inf")
  }
}

rmse <- function(y, prediction) {
  validate_pair(y, prediction)
  sqrt(mean((y - prediction)^2))
}

mae <- function(y, prediction) {
  validate_pair(y, prediction)
  mean(abs(y - prediction))
}

r2 <- function(y, prediction) {
  validate_pair(y, prediction)
  denominator <- sum((y - mean(y))^2)
  if (denominator == 0) stop("R-squared denominator is zero")
  1 - sum((y - prediction)^2) / denominator
}

fit_ridge <- function(data, features, alpha) {
  if (length(features) == 0) stop("Frozen feature list is empty")
  x <- as.matrix(data[, features, drop = FALSE])
  y <- data[[target]]
  if (any(!is.finite(x)) || any(!is.finite(y))) stop("Training data contain NA or Inf")

  means <- colMeans(x)
  centered <- sweep(x, 2, means, FUN = "-")
  scales <- sqrt(colMeans(centered^2))
  scales[scales == 0] <- 1
  standardized <- sweep(centered, 2, scales, FUN = "/")
  y_mean <- mean(y)
  gram <- crossprod(standardized) + alpha * diag(ncol(standardized))
  beta <- solve(gram, crossprod(standardized, y - y_mean))

  list(
    features = features,
    alpha = alpha,
    means = means,
    scales = scales,
    beta = as.numeric(beta),
    intercept = y_mean
  )
}

predict_ridge <- function(model, data) {
  x <- as.matrix(data[, model$features, drop = FALSE])
  if (any(!is.finite(x))) stop("Prediction data contain NA or Inf")
  standardized <- sweep(sweep(x, 2, model$means, FUN = "-"), 2, model$scales, FUN = "/")
  as.numeric(model$intercept + standardized %*% model$beta)
}

models <- list(
  "Classical Ridge" = fit_ridge(training, classical, 300),
  "Primary Lambda + characters + residue energy" = fit_ridge(training, candidate, 3000),
  "Secondary lagged Lambda" = fit_ridge(training, secondary, 1000)
)
predictions <- lapply(models, predict_ridge, data = test)
y <- test[[target]]

model_rows <- data.frame()
for (name in names(models)) {
  prediction <- predictions[[name]]
  model_rows <- rbind(
    model_rows,
    data.frame(
      model = name,
      feature_count = length(models[[name]]$features),
      alpha = models[[name]]$alpha,
      rmse = rmse(y, prediction),
      mae = mae(y, prediction),
      r2 = r2(y, prediction),
      check.names = FALSE
    )
  )
}

classical_prediction <- predictions[["Classical Ridge"]]
primary_prediction <- predictions[["Primary Lambda + characters + residue energy"]]
secondary_prediction <- predictions[["Secondary lagged Lambda"]]
overall_delta <- rmse(y, classical_prediction) - rmse(y, primary_prediction)

ordered_families <- c("x^0.5", "x^0.666667", "x^0.75")
if (!setequal(unique(test$family), ordered_families)) stop("Unexpected Dataset 003 families")

family_rows <- data.frame()
family_delta <- numeric(length(ordered_families))
names(family_delta) <- ordered_families
for (family in ordered_families) {
  index <- which(test$family == family)
  if (length(index) != 160) stop("Unexpected family size")
  delta <- rmse(y[index], classical_prediction[index]) -
    rmse(y[index], primary_prediction[index])
  family_delta[[family]] <- delta
  family_rows <- rbind(
    family_rows,
    data.frame(
      family = family,
      n = length(index),
      classical_rmse = rmse(y[index], classical_prediction[index]),
      primary_rmse = rmse(y[index], primary_prediction[index]),
      secondary_rmse = rmse(y[index], secondary_prediction[index]),
      primary_delta = delta,
      check.names = FALSE
    )
  )
}

park_miller_modulus <- 2147483647
park_miller_multiplier <- 16807
state <- 20260712
replicates <- 10000
bootstrap_delta <- numeric(replicates)
family_indices <- lapply(ordered_families, function(family) which(test$family == family))

for (replicate in seq_len(replicates)) {
  sample_index <- integer(0)
  for (indices in family_indices) {
    draws <- integer(length(indices))
    for (position in seq_along(indices)) {
      state <- (park_miller_multiplier * state) %% park_miller_modulus
      draws[[position]] <- indices[[(state %% length(indices)) + 1]]
    }
    sample_index <- c(sample_index, draws)
  }
  bootstrap_delta[[replicate]] <-
    rmse(y[sample_index], classical_prediction[sample_index]) -
    rmse(y[sample_index], primary_prediction[sample_index])
}

interval <- unname(quantile(bootstrap_delta, c(0.025, 0.5, 0.975)))
probability_better <- mean(bootstrap_delta > 0)
family_stable <- all(family_delta > 0)

if (overall_delta > 0 && interval[[1]] > 0 && family_stable) {
  decision <- "REPLICATED CANDIDATE SIGNAL"
} else if (overall_delta > 0 && interval[[1]] > 0 && !family_stable) {
  decision <- "HETEROGENEOUS EXPLORATORY REPLICATION — NOT PROMOTED"
} else if (interval[[3]] <= 0) {
  decision <- "NEGATIVE INDEPENDENT REPLICATION"
} else {
  decision <- "UNRESOLVED IN INDEPENDENT REPLICATION"
}

prediction_table <- test[, c("window_id", "family", "start", "end", "h", target)]
prediction_table$pred_classical <- classical_prediction
prediction_table$pred_primary <- primary_prediction
prediction_table$pred_secondary <- secondary_prediction

bootstrap_row <- data.frame(
  overall_delta = overall_delta,
  bootstrap_ci_lower = interval[[1]],
  bootstrap_median = interval[[2]],
  bootstrap_ci_upper = interval[[3]],
  probability_better = probability_better,
  family_stable = family_stable,
  decision = decision,
  check.names = FALSE
)

write.csv(model_rows, file.path(output_dir, "r_model_results_003.csv"), row.names = FALSE)
write.csv(family_rows, file.path(output_dir, "r_family_results_003.csv"), row.names = FALSE)
write.csv(prediction_table, file.path(output_dir, "r_predictions_003.csv"), row.names = FALSE)
write.csv(bootstrap_row, file.path(output_dir, "r_bootstrap_003.csv"), row.names = FALSE)

print(model_rows)
print(family_rows)
print(bootstrap_row)
