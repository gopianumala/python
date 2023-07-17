'''
rent is at high in the month of 4,5,6,11,12.
upto 20%
'''
m=int(input())
c=int(input())
d=int(input())
if(m==4 or m==5 or m==6 or m==11 or m==12):
    h=(20/100)*c
    t=h+c
    print('%.2f'%(d*t))
else:
    print('%.2f'%(d*c))
