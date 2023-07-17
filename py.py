'''def sumlist(List):
    sum=0
    k=[]
    for i in List:
        sum=sum+i
        k.append(sum)
    return k
s=list(map(int,input().split()))
#s=[1,2,3,4]
print(sumlist(s))

def sqrt(List):
    p=0
    for i in List:
        p=p+i*i
    return p
k=list(map(int,input().split()))
print(sqrt(k))

def in_array(array1, array2):
    array3=[]
    for i in range(len(array1)):
        for j in range(len(array2)):
            if(array1[i]==array2[j]):
                array3.append(array1[i])
            else:
                pass
    return array3
k1 = ["arp", "mice", "bull"] 
k2 = ["lively", "alive", "harp", "sharp", "armstrong"]
k1=list(map(str,input().split()))
k2=list(map(str,input().split()))
print(in_array(k1,k2))'''

def spin_words(s):
    m=[]
    k=s.split()
    for i in k:
        if(len(i)>4):
            m.append(i[::-1])
        else:
            
            m.append(i)
    h=""
    for i in m:
        h=h+i+" "
    return h
o="welcome"
print(spin_words(o))


