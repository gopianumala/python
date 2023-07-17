n=int(input())
for i in range(0,n+1):
    for j in range(1,n):
        
        if(i==j)or j==(n-i)or i==j==(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            
    print()
