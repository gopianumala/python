x = int(input())
n = int(input())
s = 1
nr = 1
for i in range(1,n+1):
    nr = ((nr**x)/i)
    print(nr)
    s+=nr
print("The sum of the series: ",s)
