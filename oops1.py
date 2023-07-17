'''
-------------------------------------------------------------
multi-inheritance
-------------------------------------------------------------

class A:
    gname="rama"
class B(A):
    fname="sitharamaraju"
class C(B):
    cname="ajay"
class D(C):
    gname="rama"
    def display(self):
        print(self.gname,self.fname,self.cname)
obj=D()
obj.display()

----------------------------------------------------------
herarical
----------------------------------------------------------
class A:
    gname="rama"
class B:
    fname="sitharamaraju"
class C(A,B):
    def display(self):
        print(self.gname,self.fname)
obj=C()
obj.display()

-----------------------------------------------------------
multiple
-----------------------------------------------------------

class A:
    Fname="rama"
    sname="k"
class C1(A):
    c1name="vjay"
    def display(self):
        print(self.Fname,self.sname,self.c1name)
class C2(A):
    c2name="ajay"
    def display(self):
        print(self.Fname,self.sname,self.c2name)
obj1=C1()
obj2=C2()
obj1.display()
obj2.display()

-------------------------------------------------------------

-------------------------------------------------------------
'''

