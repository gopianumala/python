n=int(input())
k=0
sum=0

while(n>0):
    k=n%10
    n=n//10
    sum=sum+k
print(sum)
