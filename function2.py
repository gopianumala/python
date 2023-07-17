def fib(n):
    a=0
    b=1
    c=0
    print(a,b,end=" ")
    i=0
    while n>i:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        i=i+1
       
n=int(input())   
fib(n)       
