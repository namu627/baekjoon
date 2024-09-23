import sys
n,m=map(int,sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
a.sort()
start=1
end=a[-1]
ans=0
while start<=end:
    mid=(start+end)//2
    tree=0
    for i in a:
        if mid<i:
            tree=tree+(i-mid)
    if tree<m:
        end=mid-1
    else:
        ans=mid
        start=mid+1
print(ans)