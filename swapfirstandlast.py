'''n= int(input())
k=[]
for i in range(0,n):
    a=int(input())
    k.append(a)

i=k[-1]
j=k[0]
k[0]=i
k[-1]=j
print(k)

n= int(input())    
m=list(map(int,input().split()))[0:n]
i=m[0]
j=m[-1]
m[0]=j
m[-1]=i
print(m)
'''
n= int(input())
m=[int(input())for i in range(0,n)]
print(type(m))
m[0],m[-1]=m[-1],m[0]
print(m)

