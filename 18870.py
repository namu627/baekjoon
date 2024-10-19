import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
index=sorted(set(arr))
# 시간초과로 틀림
# for i in range(len(index)):
#     for j in range(n):
#         if arr[j]==index[i]:
#             arr[j]=i
dic={} #2중for문 쓰면 시간초과 나와서 딕셔너리 쓰기로 함
for i in range(len(index)):
    dic[index[i]]=i
for i in arr:
    print(dic[i], end=' ')
