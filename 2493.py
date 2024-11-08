import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
stack=[]
ans=[]
a=1
for i in range(n):
    while stack:
        if arr[i]<=stack[-1]:
            ans.append(stack)
print(ans)