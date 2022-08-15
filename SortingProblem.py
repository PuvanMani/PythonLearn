
#Remove a Duplicate Element Then
#Sort and Add the Element into List Then Sort then Conver into String


#Calculating a lenth
def lenth(val):
    count=0
    for i in val:
        count+=1
    return count

#Soriting a List (Bubble Sort Algorithm)
def sor(s):
    strt=0
    for i in range(strt,lenth(s)-1):
        for j in range(lenth(s)-1):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
            strt+=1
    return s


#Getting Input
inp=input("Enter Text Here :")
out=''
li=[]

#Remove Duplicate value
if inp not in out:
    out+=inp
print("\nAfter Removing Duplicate :",out)

#Sorting a List
for i in out:
    li+=i
    arrange=sor(li)
print("\nSorted List=",arrange)

#Conver List To String
final=''
for i in li:
    final+=i
print("\nAfter Sorted String :",final)
