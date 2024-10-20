import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split())) #2 4 -10 4 -9
arr2=sorted(set(arr)) #중복제거하고 오름차순 정렬해서 리스트만듦. -10 -9 2 4 
# 시간초과로 틀림
# for i in range(len(arr2)):
#     for j in range(n):
#         if arr[j]==arr2[i]:
#             arr[j]=i
dic={} #2중for문 쓰면 시간초과 나와서 딕셔너리 쓰기로 함
for i in range(len(arr2)): #i=0~3
    dic[arr2[i]]=i #{-10: 0, -9: 1, 2: 2, 4: 3}
for i in arr:
    print(dic[i], end=' ') #arr 값 돌면서 딕셔너리에 저장된 key값으로 value값 출력하기
