li=[1,5,7,3,2,70,47,22,45,1,39,23,54,62,78,52]
strt=0
for j in range(strt,len(li)-1):
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            li[i],li[i+1]=li[i+1],li[i]
    strt+=1
print(li)

