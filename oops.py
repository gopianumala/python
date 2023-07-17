class Semester1:
    def __init__(self,subjs,cga):
        self.subjs=subjs
        self.cga=cga
    def display(self):
        print("your subjs is :",self.subjs)
        print("your cga is :",self.cga)
class Semester2(Semester1):
    def __init__(self,subjs,cga):
        self.subjs=subjs
        self.cga=cga
subjs=5
cga=7
#obj=Semester1(subjs,cga)
obj1=Semester2(subjs,cga)
obj1.display()
    
        
