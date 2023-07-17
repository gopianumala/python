'''dic2={}
K=[]
L=[]
s=0
l=0
q=0
Q=0
S=0
while(True):
    a=input()
    if(a=="STOP"):
        break
    else:
        K.append(a)
        b=int(input())
        L.append(b)
        dic1={a:b}
        dic2.update(dic1)

print(L)
print(K)
print(K[0])
print(K[1])
'''
s=0
l=0
q=0
Q=0
S=0
L=[7, 8, 6, 9]
K=['Up', 'Down', 'Left', 'Right']
Z=len(K)
print(Z)
for i in range(0,3):
        if(K[i]=='Right' and K[i+1]=="left"):
             s=L[i]-L[i+1]
        elif(K[i]=='Up' and K[i+1]=='Down'):
            q=L[i]-L[i+1]
        elif(K[i]=='Right' and K[i+1]=="Right"):
            Q=L[i]+L[i+1]
        elif(K[i]=='Left' and K[i+1]=="Left"):
            S=L[i]+L[i+1]
print(S,Q,s,q)
