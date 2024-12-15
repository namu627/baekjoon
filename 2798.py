from itertools import permutations
n,m=map(int,input().split())
card=list(map(int,input().split())) #n장의 카드들
ans=[]
for i in permutations(card,3):
    if sum(i)<=m:
        ans.append(sum(i))
print(max(ans))