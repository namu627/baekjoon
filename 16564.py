N,K=map(int, input().split())
x=[]
#이분탐색 안쓰고 최소값에 1씩 더해서 찾는 방법인데 시간초과뜸
# for _ in range(K):
#      x[x.index(min(x))]=min(x)+1
#      K=K-1
# print(min(x))
for _ in range(N):
     x.append(int(input()))
while K>1:
    start=min(x)
    end=max(x)
    mid=(start+end)//2
    if start<mid:
        x[x.index(min(x))]=mid
        K=K-(mid-start)
print(min(x))