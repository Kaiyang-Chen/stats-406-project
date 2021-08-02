T=readtable("influence_data.csv");
s=T.influencer_id;
t=T.follower_id;
names=[T.influencer_name,T.follower_id];
EdgeTable = table([s t],'VariableNames',{'EndNodes'});
NodeTable = table(names,'VariableNames',{'Name'});
G=digraph(EdgeTable);
plot(G)