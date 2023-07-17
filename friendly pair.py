a=int(input())
b=int(input())
s=z=0
for i in range(1,a+1):
    if(a%i==0):
        s=s+i
k=a/s
for i in range(1,b+1):
    if(b%i==0):
              z=z+i
l=b/z
print("True")if(k==l) else print("False")
