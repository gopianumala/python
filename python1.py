n=int(input())
a=0
b=1
l=[0,1]
for i in range(0,n+3):
    c=a+b
    l.append(c)
    a=b
    b=c
print(l)
k=0
for i in range(0,n):
    for j in range(i):
        print(l[k],end=" ")
        k=k+1
    print()    

