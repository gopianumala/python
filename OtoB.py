n=int(input())
list1=[]
while(n>0):
    k=n%10
   # print(k)
    def DtoB(a):
        list=[]
        while a>0:
            m=a%2
            print(m)
            list.append(m)
            a=a//2
        list=(list[::-1])
        if(len(list)!=3):
               for i in range(3-len(list)):
                       list.insert(0,0)
        return(list)
    n=n//10
    l=DtoB(k)
    list1.append(l)
o=(list1[::-1])
list2=[]
for i in o:
    list2.extend(i)
print(list2)
    
    
