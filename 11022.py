t=int(input())
ans=[]
for i in range(1, t+1):
    a,b=map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i,a,b,a+b)) #문자열 이렇게 포맷팅할 수 있음