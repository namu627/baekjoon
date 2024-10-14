a,b=map(int, input().split())
c=int(input())

b=b+c
if b>=60:
    a=a+b//60
    b=b%60
if a>=24:
    a=a%24
print(a,b)