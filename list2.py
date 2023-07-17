n=int(input("N0. of inputs:"))
l=[]
for i in range(1,n+1):
    a=input("enter {} element:".format(i))
    l.append(int(a))
print("Max :",max(l))
print('Min :',min(l))
print("sum :",sum(l))
