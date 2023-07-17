a=int(input())
x=1
for i in range(1,a+1):
    
    
    if(i!=a):
        for j in range(0,x):
            print(" ",end=" ")
        x=x+1
        for k in range(1,2*a-2):
            print("*",end=" ")
        a=a-1
        print("\n")
    
 '''       
        

  * * * * * * * 

    * * * * * 

      * * * 

        * 
'''

