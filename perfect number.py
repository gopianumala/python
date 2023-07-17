n=int(input())
k=0
m=n
for i in range(1,n):
    if(n%i==0):
        k=k+i
print("perfect number ")if(k==m) else print("Not perfect number")
