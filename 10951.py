ans=[]
while True:
    try: #try는 에러가 발생할 가능성이 있는 코드를 실행시 쓰고
        a,b=map(int,input().split())
        ans.append(a+b)
    except: #에러가 발생하면 이렇게 해라 라고 하는것이 except이다
        break 
for i in ans:
    print(i)