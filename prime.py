n=int(input())
k=1
def fact(n):
    if(n==1 or n==0):
       # k = 1
    else:
        
      k= n*fact(n-1)
      print(k)
print(k)
