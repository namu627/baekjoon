import sys

limit=123456 *2 #에라토스테네스의 체로 미리 소수 구해놓기
is_prime=[True]*(limit+1)
is_prime[0]=is_prime[1]=False

for i in range(2, int(limit**0.5)+1): #2부터 limit의 제곱근까지만 보면 댐
    if is_prime[i]:
        for j in range(i*i, limit+1, i):
            is_prime[j] = False 

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break

    print(sum(is_prime[n+1:2*n+1]))