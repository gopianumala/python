import math
sum=0
n=int(input())
m=n
while(n>0):
    k=n%10
    sum=sum+math.factorial(k)
    n=n//10
print("True")if(m==sum) else print("False")
    
