a=int(input())
b=int(input())
def arms(n):
    arm=0
    while(n>0):
         k=n%10
         arm=arm+k**3
         n=n//10
    return arm
for i in range(a,b+1):
             k=arms(i)
             if(k==i):
                 print(i)

    
    
    
