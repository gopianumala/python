a=list((1,2,3,5))
print("#len function")

print(len(a))
print("#slicing")
print(a[0:])
print(a[0:-1])
print(a[0::1])
print(a[0::2])
print(a[0::-2])
print("#insert #append # extend")
k=[1,2,3]
print(k)
k.append((4))
print(k)
k.insert(4,4)
print(k)
k.extend([5,6,7,8])
print(k)
k.append([1,2,3])
print(k)
k.append([11])
print(k)
print("#replace by using index")

e=[1,2,3]
e[2]=6
print(e)

print("# remove # pop #del #clear")
k=[1,2,3,4,5,6]
print(k)
k.remove(3)
print(k)
k.pop(3)
print(k)
#k.del(0:2)
print(k)

