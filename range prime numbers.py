a=int(input())
def is_prime(n):
    if(n<2):
        return False
    c=1
    for i in range(2,n):
            if(n%i==0):
                c=c+1
    if(c==1):
        return True
    else:
        return False
for i in range(a+1):
   k=is_prime(i)
   if(k==True):
       print(i)
        

