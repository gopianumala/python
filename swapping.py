''' swapping without   3rd variable '''
a=int(input())
b=int(input())
'''
a=a^b
b=b^a
a=a^b
'''

a=a+b
b=a-b
a=a-b

'''
a,b=b,a
'''

print(a)
print(b)
''' swapping with   3rd variable '''
t=a
a=b
b=t 
print(a)
print(b)

