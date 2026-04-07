t=int(input())

prime=[True for _ in range(1000001)] #에라토스테네스의 체로 100만까지 미리 소수 구해놓기

for i in range(2, 1000001): #2부터 1000000까지의 수 중에
    if prime[i]==True: #소수인 수의 배수는 소수가 아니므로
        for j in range(i*2, 1000001, i): #i의 2배부터 1000000까지 i씩 증가하면서
            prime[j] = False #소수가 아닌 수는 False로 바꿔줌

for _ in range(t):
    n=int(input())

    partition=0 #골드바흐 파티션 수
    for i in range(2, n//2+1): #2부터 n의 절반까지의 수 중에
        if prime[i] and prime[n-i]: #i와 n-i가 모두 소수이면
            partition+=1 #골드바흐 파티션 수 증가
    print(partition)