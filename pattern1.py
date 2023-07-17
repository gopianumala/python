r=int(input())
c=int(input())
for i in range(r,0,-1):
    for j in range(1,c+1):
        print(i,end=" ")
    print()
'''
r->1      j      r+1,0,-1   and    (c+1,0,-1)
l->1      j      0,r+1,1    and     0,c+1
t->1      i      0,r+1,1     and     0,c+1
b->1      i      r+1,0,-1    and     0,c+1

'''
