import math
a,b,v=input().split()
a=int(a)
b=int(b)
v=int(v)
x=1
if (v-a) <= 0:
    print(x)
else:
    x=math.ceil((v-a)/(a-b))+1
    print(x)