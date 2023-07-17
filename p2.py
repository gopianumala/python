n=input()
def db(n):
    def dtob(n):
     c=[]
     while n>0:
      a=n%2
      c.append(a)
      n=n//2
     return c
    count=0
    s=0
    w=set()
    for i in range(len(n)):
            k=dtob((int(n[i])))
            w.update(set(k))
            s=s+k.count(1)
    print(w)
    return s
print(db(n))

