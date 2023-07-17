n=int(input())
a,b=0,1
list=[0,1]
for i in range(n):
    c=a+b
    a=b
    b=c
    list.append(c)
print(list)
    
    
