n=int(input())
c=0
for i in range(1,n+1):
    sum=i
    for j in range(i+1,n+1):
        sum+=j
        if(sum==n):
            print(i,end=" ")
            for k in range(i+1,j+1):
                print("+",k,end=" ")
            print("=",sum)
            c+=1
print(c)
