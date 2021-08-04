

influ_page_rank_0.1 <- influence_page_rank_0_0_0

n <- nrow(influ_page_rank_0.1)
null_distribution <- replicate(10000, {
  rx <- sample(1:n)
  cor(rx, 1:n)
})
cor_obs <- with(influ_page_rank_0.1, cor(rank(influ_page_rank_0.1$influence_score), rank(influ_page_rank_0.1$out_degree)))
2 * min(mean(null_distribution < cor_obs),
        mean(null_distribution > cor_obs))
ggplot(data.frame(x = null_distribution), aes(x = x)) + geom_density(fill = "blue", alpha =0.5)+xlab("Permutation Test Statistic")+ylab("Density")
