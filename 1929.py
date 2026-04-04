m,n=map(int,input().split())

for i in range(m, n+1):
    if i==1:
        continue

    for j in range(2, int(i**0.5)+1): #2부터 i의 제곱근까지만 보면 댐
        if i%j==0:  #i가 j로 나누어 떨어진다면 소수가 아님
            break
    else:
        print(i)