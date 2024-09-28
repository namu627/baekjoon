import sys

n=int(sys.stdin.readline())
a=[]
f=[0]*10001 #도수 카운트 리스트. 10000자리까지 0으로 초기화 시킨다는 뜻

for i in range(n):
    x=int(sys.stdin.readline())
    f[x]=f[x]+1 #입력받은 수 의 리스트 위치에 숫자 1개씩 더하기
for i in range(1,10001): #1부터 10000까지
    if f[i]>=1: #1개 이상인거 있으면
        for j in range(f[i]): #그 수만큼 반복출력
            print(i)