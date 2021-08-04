### R code from vignette source '/Users/mark/Documents/Professional/Teaching/sjtu/stats406-summer2021/lectures/week08/week08_permutation_randomization_advanced/lecture-core.Rnw'

#
options(width = 60, digits = 4)
set.seed(49482)
library(tidyverse)
library(ggplot2)


all_music <- read.csv("./2021_ICM_Problem_D_Data_std/full_music_data.csv", header = TRUE)
for(i in 3:13){
  first <- all_music[,i]
  for (j in (i+1):14){
    second <- all_music[,j]
    observed_cor <- with(all_music, cor(first, second))
    cors <- replicate(1000,{
      shuffled_second <- sample(second)
      cor(first, shuffled_second)
    })
    res <- (2*min(mean(cors >= observed_cor), mean(cors <= observed_cor)))
    print(i)
    print(j)
    print(res)
  }
}
    
  
popularity <- unlist(all_music[16])
acou <- unlist(all_music[10])
fit1 <- lm(popularity~acou)
summary(fit1)

for(i in 3:13){
  first <- unlist(all_music[,i])
  for (j in (i+1):14){
    second <- unlist(all_music[,j])
    fit <- lm(first~second)
    if(summary(fit)[8]>0.5){
      print(i)
      print(j)
      print(summary(fit)[8])
    }
    
  }
}


for (j in 3:14){
  first <- unlist(all_music[,16])
  second <- unlist(all_music[,j])
  fit <- lm(first~second)
  print(summary(fit)[8])
  if(summary(fit)[8]>0.5){
    print(i)
    print(j)
    print(summary(fit)[8])
  }
  
}

ggplot(data = all_music, aes(x = loudness, y = energy)) + geom_point(alpha = 0.5)+ geom_smooth(aes(x = loudness, y = energy), method = "lm", color = "red")


predictors <- c("danceability",
                "energy",
                "key",
                "loudness",
                "speechiness",
                "acousticness",
                "instrumentalness",
                "liveness",
                "tempo",
                "valence")
tracks_tall <- pivot_longer(music, cols = predictors[-9])
ggplot(tracks_tall, aes(x = value, y = popularity)) + geom_point(size = 0.25) + facet_wrap(~ name, scales = "free_x")
