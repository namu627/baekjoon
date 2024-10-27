import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
stack=[]
for i in range(n):
    for j in range(i,-1,-1):
        if arr[i]<arr[j]:
            stack.append(j+1)
            break
    if len(stack)<i+1:
        stack.append(0)
print(stack)