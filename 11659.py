n,m=map(int,input().split())
n_list=list(map(int,input().split()))
ans=[]
for _ in range(m):
    a,b=map(int,input().split())
    ans.append(sum(n_list[a-1:b])) #a~b까지 합 (인덱스 번호라서 -1)

for i in ans:
    print(i)