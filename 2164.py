from collections import deque
import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(i+1)
arr=deque(arr)
while len(arr)>1:
    arr.popleft()
    arr.rotate(-1)
print(arr[0])