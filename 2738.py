n,m=map(int, input().split())
arr1=[] #2차원 배열1
arr2=[] #2차원 배열2
for _ in range(n):
    a=list(map(int, input().split())) #입력받은거 리스트로 만들어서 배열에 리스트째로 넣기
    arr1.append(a)
for _ in range(n):
    a=list(map(int, input().split()))
    arr2.append(a)
for i in range(n):
    for j in range(m):
        print(arr1[i][j]+arr2[i][j], end=' ')
    print('')
