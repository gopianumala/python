n=int(input())
def add(n):
    if(n==1):
        return 1
    else:
        if(n%2==0):
             return (n-1)+add(n-3)
        else:
            return n+add(n-2)
print(add(n))
