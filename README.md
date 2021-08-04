# README

## Project: The influence of music

#### Project Member: Kaiyang Chen, Baole Fang, Yumeng Bai



## Filetree

```
.
├── 2021_ICM_Problem_D_Data
├── 2021_ICM_Problem_D_Data_std
├── fang
│   ├── 2021_ICM_Problem_D_Data
│   ├── 2021_ICM_Problem_D_Data_edit
│   └── Step\ 1
│       ├── heat_map
│       ├── heat_map_sub
│       ├── in_degree
│       ├── in_degree_sub
│       ├── music_network_sub
│       ├── out_degree
│       ├── out_degree_sub
│       ├── page_rank_result
│       └── page_rank_result_sub
├── step2
├── step3
│   ├── original
│   └── std
└── step4
```
## Step1

Use influence_page_rank.py to implement PageRank algorithm and plot relevant figures. 

Then use permutation_test_ranking.R to do permutation tests on the two rankings.

Visual.py is used to generate influencial network plots.


## Step2

Use `python PvaluePlot.py` to generate the 2-tail p-value matrix for feature pairs.

Run the code trunk in FeatureAnalysis.R step by step to get the analysis result.

## Step 3: Measure of musical similarity

### Overview

In this step, we purpose a measure of musical similarity. We perform a permutation test to verify its validness. The null hypothesis is that the music genres are independent of musical features.

One assumption we make is that songs/musicians within the same genre are more similar than those between different genres. If we can reject the null hypothesis, it means that our measure of musical similarity is valid.

### Data

- [data_by_artist.csv](2021_ICM_Problem_D_Data_std/data_by_artist.csv)
- [influence_data.csv](2021_ICM_Problem_D_Data_std/influence_data.csv)

### How to run

1. Run [MCC.py](step3/MCC.py) and get [artists.csv](step3/std/artists.csv), [clusters.csv](step3/std/clusters.csv)

To run scripts successfully:
- Please specify the path of input and output
- Please install the necessary packages by yourself

### Results

![](step3/std/MCC.jpeg)
![](step3/std/MCC_PermutationTest.jpeg)

## Step 4: Influence and similarity

### Overview

In this step, we analyze the relationship between musical influence and similarity. We perform a stratified bootstrap to find the confidence interval of the difference of SS mean. If the confidence interval lies above 0, it means that high-influential musicians have a stronger impact on their followers.

### Data

- [influence_page_rank_0.5_0.csv](step4/influence_page_rank_0.5_0.csv)

### How to run

1. Run [SS.py](step4/SS.py) and get [SS.csv](step4/SS.csv)
2. Replace "0.0" in [SS.csv](step4/SS.csv) with "nan" (data cleaning)
3. Run [bootstrap.R](step4/bootstrap.R) to compute the confidence interval

To run scripts successfully:
- Please specify the path of input and output
- Please install the necessary packages by yourself

### Results

![](step4/SS.png)
