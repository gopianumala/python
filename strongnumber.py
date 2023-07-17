import math
n=int(input())
k=n
T=0
while n>0:
    a=n%10
    n=n//10
    T=T+math.factorial(a)
if(T==k):
    print("   Strong Number")
else:
    print("Not  Strong Number")
