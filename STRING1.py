n=input()
c=0
s=0
for i in n:
    if(i>='a' and i<='z'):
        c=c+1
    elif(i>='A' and i<='Z'):
        s=s+1
print("count of lower case {},count of uppercase {}".format(c,s))
