print("please select from the menu\na.Arithematic\nb.comparision\nc.logical\nd.Bitwise")
n=input()

if(n=='a'):
    print("Please Enter the option :\n1.+ add\n2.- sub\n3./ div\n4.* multiplication\n5.Back To menu")
    k=int(input())
    n1=int(input("Enter the number-1 :"))
    n2=int(input("Enter the number-2 :"))
    if(k==1):
        def add(n1,n2):
            return n1+n2
        print(add(n1,n2))
    elif(k==2):
           def sub(n1,n2):
                return n1-n2
           print(sub(n1,n2))
    elif(k==3):
        
         def div(n1,n2):
             return n1/n2
         print(div(n1,n2))
    elif(k==4):
          def mult(n1,n2):
                return n1*n2
          print(mult(n1,n2))
    
        
elif(n=='b'):
    print("Please enter the options:\n1.islessthan\n2.isgreaterthan\n3.isequal\n")
    k=int(input())
    n1=int(input("Enter the number-1 :"))
    n2=int(input("Enter the number-2 :"))
    if(k==1):
          def islesser(n1,n2):
                   return n1<n2
          print(islesser(n1,n2))
    elif(k==2):
        def isgreater(n1,n2):
            return n1>n2
        print(isgreater(n1,n2))
    elif(k==3):
        def isequal(n1,n2):
            return n1==n2
        print(isequal(n1,n2))
elif(n=='c'):
    print("Please enter the options:\n1.And\n2.Or\n3.Not")
    k=int(input())
    n1=int(input("Enter the number-1 :"))
    n2=int(input("Enter the number-2 :"))
    if(k==1):
        def And(n1,n2):
            return n1 and n2
        print(And(n1,n2))
    elif(k==2):
        def Or(n1,n2):
            return n1 or n2
        print(Or(n1,n2))
    elif(k==3):
        def Not(n1,n2):
            return n1
        print(Not(n1,n2))
elif(n=='d'):
    print("Please enter the options:\n1.&(and)\n2.|(or)\n3.^(Xor)\n4.rightshift\n5.leftshift")
    k=int(input())
    n1=int(input("Enter the number-1 :"))
    n2=int(input("Enter the number-2 :"))
    
    if(k==1):
        def And(n1,n2):
            return n1 & n2
        print(And(n1,n2))
    elif(k==2):
        def Or(n1,n2):
            return n1 | n2
        print(Or(n1,n2))
    elif(k==3):
        def X(n1,n2):
            return n1 ^ n2
        print(X(n1,n2))
    elif(k==4):
        def R(n1,n2):
            return n1>>n2
        print(Not(n1,n2))
    elif(k==5):
        def L(n1,n2):
            return n1>>n2
        print(L(n1,n2))
print("THANK YOU")
    
          
        

      







