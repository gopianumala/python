'''
1 same
2 50%ht
3 2ht
4 not recommed
'''
item=int(input())
ht=float(input())
if(item==1):
    print('%.2f'%ht)
elif(item==2):
    ht=((50/100)*ht)+ht
    print('%.2f'%ht)
elif(item==3):
    ht=2*ht
    print('%.2f'%ht)
else:
    print("Not recommend")
