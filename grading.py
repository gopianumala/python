M=int(input())
if(M>=1 and M<=100):
    if(M>=90 and M<100):
        print("A")
    elif(M>=80 and M<90):
        print("B")
    elif(M>=70 and M<80):
        print("C")
    elif(M>=60 and M<70):
        print("D")
    elif(M>=50 and M<60):
        print("E")
    else:
        print("F")
else:
    print("Invalid")
