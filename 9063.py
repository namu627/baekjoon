n=int(input())
x=[]
y=[]
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
if n==1:
    print(0)
else:
    print((max(x)-min(x))*(max(y)-min(y))) #각 x,y좌표에서 가장 큰값에서 가장 작은값 뺀 수끼리 곱하면 답임