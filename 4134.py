import sys
input = sys.stdin.readline

#에라토네스의 체를 사용해서 미리 소수들 구해놓기(루트 40억인 63245까지)
limit = 64000 #넉넉잡아
is_prime_list = [True] * (limit + 1) #다 true로 초기화
is_prime_list[0] = is_prime_list[1] = False #0과 1은 소수가 아니므로 false로 설정
for i in range(2, int(limit**0.5) + 1): #2부터 루트 limit까지 돌면서
    if is_prime_list[i]:
        for j in range(i*i, limit + 1, i): #i의 배수들을 false로 설정
            is_prime_list[j] = False #i의 배수들은 소수가 아니므로 false로 설정

primes = [i for i, v in enumerate(is_prime_list) if v] #소수들만 리스트에 담아두기

def is_prime(n): #소수 판별 함수
    if n < 2: return False
    #소수 리스트를 순회하며 n의 약수가 있는지 확인
    for p in primes:
        if p * p > n: break #루트 n까지만 확인하면 충분
        if n % p == 0: return False #n이 p로 나누어 떨어지면 소수가 아님
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1