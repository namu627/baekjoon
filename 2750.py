n=int(input())
a=[]
for i in range(n):
    a.append(input())
for j in range(n-1):
    for i in range(n-1):
        if int(a[i]) > int(a[i+1]):
            x=a[i]
            a[i]=a[i+1]
            a[i+1]=x
            
for i in range(n):
    print(a[i])