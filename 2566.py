arr=[list(map(int, input().split())) for i in range(9)] #9x9 2차원배열 입력받기
print(max(map(max, arr))) #max를 통해서 최대값 찾기. 2차원 배열이기 때문에 map 함수를 통해 감싸준 모습
max=arr[0][0] #일단 최대값 0,0값으로 임시 설정
a=b=0 #a는 행, b는 열
for i in range(9): #반복문으로 하나씩 보면서
    for j in range(9):
        if arr[i][j]>=max:
            max=arr[i][j] #최대값 찾으면 max값 변경하고 
            a=i+1 #좌표찍기
            b=j+1
print(a,b)