n=input("Enter the octal bits:")
j=0
for i in range(1,len(n)+1):
    k=n[-i]
    m=int(k)*(8**(i-1))
    j=j+m
print(j)

      
