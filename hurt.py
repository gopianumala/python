n=int(input())
k=n
c=k+1//2

for i in range(0,k+1):
    for j in range(0,k+1):
        if(j==c)or i+j==3 or j-i==3 or i==k :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for  i in range(0,n+1):
    for j in range(0,n+1):
        if(j==0 or i==n or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

