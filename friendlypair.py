n1=int(input())
n2=int(input())
sum1=0
sum2=0
for i in range(1,n1+1):
    if((n1%i)==0):
        sum1=i+sum1
for i in range(1,n2+1):
    if((n2%i)==0):
        sum2=i+sum2
    
if((sum1//n1)==(sum2//n2)):
    print("Friendly pair")
else:
    print("Not Friendly pair")
    
    
