'''
left handed
right handed
front(left r1)      (right r2)
rear (right r1)      (left r1)

front or rear
1 or 2

'''
door=input("front or rear : ")
r=input("1 or 2 : ")
if(door=='front'):
    if(r==1):
        print("left")
    else:
        print("right")
else:
    if(r==1):
        print("right")
    else:
        print("left")
