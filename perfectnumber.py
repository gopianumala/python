'''
perfect number

6= 1,2,3,...factors
k=1+2+3
if k==num
then it is perfect number
'''
num=int(input())
k=0
for i in range(1,num):
    if(num%i==0):
        k=k+i

if(num==k):
    print("perfect number")
else:
    print("not perfect number")
