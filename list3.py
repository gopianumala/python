
n=int(input())
sum=0
list1=[]
list2=[]
list3=[]
print("list1 elements :")
for i in range(0,n):
    a=int(input())
    list1.append(a)
print("list2 elements :")
for i in range(0,n):
    b=int(input())
    list2.append(b)
for i in range(0,n):
    
    sum=list1[i]+list2[i]
    list3.append(sum)
print(list3)
