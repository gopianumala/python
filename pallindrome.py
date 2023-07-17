n=int(input())
k=n
rev=0

while n>0:
    a=n%10
    n=n//10
    rev=rev*10+a
if(k==rev):
    print("pallindrome")
else:
    print("Not pallindrome")

