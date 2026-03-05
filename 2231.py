#브루트포스 분해합문제. 브루트포스: 모든 경우의 수를 다 계산하는 방법

n=int(input())
ans=0

for i in range(1, n+1):
    num=list(map(int,str(i)))
    ans=i+sum(num) #분해합 계산
    if ans==n:
        print(i)
        break
    elif i==n: #i가 n까지 다 돌았는데도 생성자가 없는 경우
        print(0)