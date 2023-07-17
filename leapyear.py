a=int(input())
#for a in range (2015 ,2030):
if(a%4==0)and (a%400==0):
      print("leap year",a)
elif(a%100!=0)and(a%4==0):
       print("leap year",a)

else:
    print("not leap year",a)
                   
