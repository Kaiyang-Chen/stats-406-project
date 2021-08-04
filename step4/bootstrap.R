# Title     : stratified bootstrap
# Objective : stratified bootstrap on the ranking
# Created by: fbl71
# Created on: 2021/8/4

library(dplyr)
library(boot)

data <- read.csv("step4/SS.csv")
data=mutate(data, influential = influential == "high")

mean_diff <- function(x, index) {
    xstar <- x[index, ] # boot will handle stratification for us
    mean(xstar$SS[xstar$influential], na.rm = TRUE) -
        mean(xstar$SS[!xstar$influential], na.rm = TRUE)
}
cancer.boot <- boot(data,
                 statistic = mean_diff,
                 strata = data$influential,
                 R = 1000)
boot.ci(boot.out = cancer.boot, type = "basic")
