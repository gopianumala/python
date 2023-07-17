n=int(input())
a1=[]
for i in range(n):
 a1.append(int(input()))

dp=[0]*201
dp[1]=10
dp[2]=55
a=[1]*10

i=3
while i<201:
 s=0
 for i1 in range(10):
   s+=a[i1]
   a[i1]=s
   dp[i]+=(s*(10-i1))
   dp[i]=dp[i]%((10**9)+7)

 i+=1

s1=0
for i in a1:
 s1+=dp[i]
 s1=s1%((10**9)+7)
