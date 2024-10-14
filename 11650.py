import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort()
for i in arr:
    print(*i)