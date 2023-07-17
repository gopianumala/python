'''
------------------------------------------------------------------

ACCESS SPECIFIERS :
-----------------
                PUBLIC ,PROTRCTED,PRIVATE
                
--------------------------------------------------------------------
'''
Gname="Thatha"
class A:
   # Gname="Thatha"
    _Fname="Nanna"
    __sname="house_name"
    def display1(self):
         print(self.Gname,self._Fname,self.c1name,self.__sname)
class B:
   # c1name="vjay"
    def display(self):
        print(self.Gname) 
        #self.display1()
obj=B()
obj.display()



'''

Polymorphisam

------------------------------------------------------------------
Method Overriding.
-------------------------------------------------------------------
'''
'''
class A:
    Gname="Thatha"
    _Fname="Nanna"
    __sname="house_name"
    def display(self):
         print(self.Gname,self._Fname,self.c1name,self.__sname)
class B(A):
    c1name="vjay"
    def display(self):
        print(self.Gname,self._Fname,self.c1name)
        self.display1()
obj=B()
obj.display()'''

