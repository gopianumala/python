n=input("Enter Your sentense :")
k=n.split()
list=[]
s=""
for i in k:
    l=i[::-1]
    list.append(l)
print(list)
for i in list:
    s=s+i+" "
print(s)
    
