n=int(input()) #n값
x=input().split() #n개의 수
y=0 #소수 개수 카운트
z=0 #소수 판별 변수
for i in range(n): #n번반복
    for j in range(2, int(x[i])): #2부터 자신-1까지 나누면서
        if int(x[i])%j == 0: #나눠떨어지는게 있으면
            z=z+1 #소수가 아니라고 표시해뒀다가
    if int(x[i])==1: #1은 소수가 아니라서 예외시키기
        z=1 #소수 아니라고 카운트+1
    if z==0: #소수 아니라는 표시가 없으면 소수
        y=y+1 #소수 카운트 +1
    z=0    
print(y)
