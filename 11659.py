import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list(map(int,input().split()))
ans=[]

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + n_list[i]

for _ in range(m):
    a,b=map(int,input().split())
    ans.append(prefix_sum[b] - prefix_sum[a-1]) #a~b까지 합 (인덱스 번호라서 -1)

print(*ans,sep='\n') #리스트를 줄바꿈으로 구분해서 출력