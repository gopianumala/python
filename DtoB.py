n=int(input())
list=[]
while n>0:
    k=n%8
    print(k)
    list.append(k)
    n=n//8
print(list[::-1])
    
