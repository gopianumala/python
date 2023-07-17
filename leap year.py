import calendar  
n=int(input())
'''if(n%4==0):
    print("leap year")
elif(n%100==0 and n%400==0):
    print("leap year")
else:
    print("Not leap year")'''
k=calendar.isleap(n)
print(k)
