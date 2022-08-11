arr=[5,10,30,24,44,50,8,3,6,1,1,1,1,1,1,3,3,3,34,5,5,5]
print('Orginal Array',arr)
x=0
strt=0
for j in range(strt,len(arr)):
    for i in range(len(arr)-1):
        if arr[x]<arr[i]:
            arr[x],arr[i]=arr[i],arr[x]
    x+=1
    strt+=1
print('Sorted Array',arr)

        
        
