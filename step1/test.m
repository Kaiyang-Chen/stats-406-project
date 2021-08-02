T=readtable("data_by_artist_delete_pca.csv");
data=readtable("C:\Users\fbl71\PycharmProjects\ICM_2021_Problem_D\Step 2\similarity_matrix.csv");
data=data{:,:};
pop=[];
others=[];
genre=T.genre;
len=length(genre);
for i=1:len
    if genre(i)==14
        pop=[pop,i];
    else
        others=[others,i];
    end
end
a=[];
b=[];
for x = pop
    for y=pop
        a=[a,data(x,y)];
    end
    for y=others
        b=[b,data(x,y)];
    end
end
[h,p,ci,stats]=ttest2(a,b,'Vartype','unequal');