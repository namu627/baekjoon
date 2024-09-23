n=int(input())
ans=0 #정답 카운트
c1=[0]*n #가로줄 체크 리스트. 범위가 0~n개까지 있음
c2=[0]*(2*n) #대각선 체크 리스트. 좌표 x+y로 체크할거라 0~6까지 2n개 있음
c3=[0]*(2*n) #반대쪽 대각선 체크 리스트. 좌표 x-y로 체크할거라 -3~3까지 2n개 있음

def nqueen(x):
    global ans #ans를 한개씩 추가할거라서 글로벌로 선언
    if x==n: #n번까지 진행하면 n개의 가로줄에 퀸이 하나씩 들어간거라서 성공한거임
        ans+=1 #그래서 성공했다고 답을 한개 올리고 종료시키기
        return
    for i in range(n): #n번 반복하면서
        if c1[i]==c2[x+i]==c3[x-i]==0: #가로줄, 대각선, 반대대각선에 퀸이 있어서 놓을수 있는지 없는지 확인해보고 0이면 없는거니까 퀸을 놓기
            c1[i]=c2[x+i]=c3[x-i]=1 #퀸 놨다고 1로 체크하고
            nqueen(x+1) #그다음줄에 퀸 놓을수 있는 자리 재귀로 탐색하기. 
            c1[i]=c2[x+i]=c3[x-i]=0 #그리고 다시 0으로 초기화

nqueen(0) #n퀸 0번째 가로줄부터 탐색할거임
print(ans)