import sys
from collections import deque

input=sys.stdin.readline


n=int(input())
a=list(map(int, input().split()))  #0=queue, 1=stack
b=list(map(int, input().split()))  #초기 원소
m=int(input())
c=list(map(int, input().split()))  #삽입할 원소들

res=deque([b[i] for i in range(n) if a[i] == 0]) #큐인 것들만 골라 deque에 담기 (역순으로) 새로운 원소가 앞(왼쪽)에서 들어오고 뒤(오른쪽)로 나가는 구조가 됨

ans = []
for x in c:
    res.appendleft(x) #새로운 원소를 앞에 넣고
    ans.append(res.pop()) #가장 뒤에 있는 원소를 추출

print(*ans) 