class A:
    Gname="Thatha"
    _Fname="Nanna"
    __sname="house_name"
    def display1(self):
         print(self.Gname,self._Fname,self.__sname)
class B:
    c1name="vjay"
    def display(self):
        print(self.Gname)
a=input()
b=input()
c=input()
d=input()
obj1=A(a,b,c)
obj1.display1()
obj=B(d)
obj.display()
