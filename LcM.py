a=int(input())
b=int(input())
k=1
for i in range(2,max(a,b)):
    for j in range(2,max(a,b)):
              if(a%i==0 and b%i==0):
                    a=a//i
                    b=b//i
                    k=i*k
print(k*a*b)
