n=int(input())
rev=0
while(n>0):
    k=n%10
    rev=k+rev*10
    n=n//10
print(rev)
    
    
    
