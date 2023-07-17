'''
conditions:
tree is at 1st row ,1st col and last col are mango trees
'''
r=int(input())
c=int(input())
tn=int(input())
if(tn>=1 and tn<=c)or(tn%c==0)or(tn%c==1):
                 print("yes")

else:
   print("No")
