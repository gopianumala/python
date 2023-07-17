
n=int(input())

list1=[]
list2=[]
list3=[]
print("list elements :")
for i in range(0,n):
    a=int(input())
    list1.append(a)
    if(a%2==0):
        
        list2.append(a)
    else:
    
        list3.append(a)
        
    
print(list2)
print(list3)
