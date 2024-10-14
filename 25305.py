n,k=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort(reverse=True) #reverse=True 를 써줌으로써 내림차순 정렬
print(arr[k-1])