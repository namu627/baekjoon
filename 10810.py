n,m=map(int,input().split())
arr=[0]*n
for x in range(m):
    i,j,k=map(int,input().split())
    for y in range(i-1,j):
        arr[y]=k
print(*arr)