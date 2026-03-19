import sys
input=sys.stdin.readline

n=int(input())
member=set()

for _ in range(n):
    a,b=map(str,input().split())
    if b=="enter": #enter면 set에 추가
        member.add(a)
    else: #아니면 제거
        member.discard(a)

member=sorted(member,reverse=True)
print(*member,sep='\n')