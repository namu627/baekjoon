n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0])) #sort 함수 설정을 저렇게 하면 두번째 값이 같을경우 첫번째 값을 기준으로 오름차순 정렬함
for i in arr:
    print(*i)