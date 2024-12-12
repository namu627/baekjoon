x=[]
y=[]
for _ in range(3):
    a,b=map(int,input().split())
    if a in x: #x좌표
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
print(*x,*y)