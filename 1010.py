#m개의 지역에 n개의 다리를 놓는 경우의수를 구하는것과 같다.
#즉 mCn을 구하는 문제. mCn=m!/(n!*(m-n)!)
def factorial(n): #팩토리얼 구현
    num=1
    for i in range(1, n+1):
        num*=i
    return num

t=int(input())

for _ in range(t):
    n,m=map(int, input().split())
    bridge=factorial(m)//(factorial(n)*factorial(m-n)) #mCn 계산
    print(bridge)