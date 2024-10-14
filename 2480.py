a=list(map(int, input().split()))
if a[0]==a[1]==a[2]:
    price=10000+a[0]*1000
elif a[0]==a[1]!=a[2]:
    price=1000+a[0]*100
elif a[0]!=a[1]==a[2]:
    price=1000+a[1]*100
elif a[0]==a[2]!=a[1]:
    price=1000+a[2]*100
else:
    price=max(a)*100
print(price)
