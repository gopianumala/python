import textwrap
n=input()
list=[]
o=n[::-1]
k=(textwrap.wrap(o, 3))
def BtoD(a):
    j=0
    for i in range(1,len(a)+1):
       k=a[-i]
       m=int(k)*(2**(i-1))
       j=j+m
    return j
for i in k:
    b=BtoD(i)
    list.append(b)
print(list)
    
      

      

