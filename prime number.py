n=int(input())
c=1
for i in range(2,n):
    if(n%i==0):
        c=c+1
print("prime")if(c==1) else print("Not prime")
    
