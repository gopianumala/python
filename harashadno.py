'''
1729
1+7+2+9=19
1729%19==0
then yes else no
'''
n=int(input())
a=n
sum=0
while n>0:
     c=n%10
     n=n//10
     sum=sum+c
     
if((a%sum)==0):
    print("Harshad")
else:
    print("Not Harshad ")

'''
n=input()
while n>0:
        a=n%10
        n=n//10
        rev=rev*10+a
'''


    

