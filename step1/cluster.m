T=readtable("data_by_artist_delete_pca.csv");
weights=[0.26324913,0.23869453,0.17307999,0.10953544,0.07253973];
X=weights.*T{:,2:6};
Y=T{:,7};
[idx,C]=spectralcluster(X,20,'Distance','correlation');