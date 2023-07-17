class MYfamily:
      def __init__(self,gname,fname,child):
              self.gname=gname
              self._fname=fname
              self._child=child
t1=MYfamily("Thatha","Nanna","son")
print(t1.gname)
print(t1._fname)
print(t1._child)

class B(MYfamily):
    def display(self):
        print(D.gname)
c=MYfamily("Thatha","Nanna","son")
print(c.gname)
print(c._fname)
print(c._child)
D=B()
D.display()

