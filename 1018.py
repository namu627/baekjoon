n,m=map(int,input().split())
board=[list(input()) for _ in range(n)]

def check(x,y):
    count=0
    for i in range(x,x+8):
        for j in range(y,y+8): #체스판 8x8크기
            if (i+j)%2==0: #체스판의 색깔이 W인 경우
                if board[i][j]!='W': #체스판의 색깔이 W인데 보드의 색깔이 W가 아니라면
                    count+=1 #count+1
            else: #체스판의 색깔이 B인 경우
                if board[i][j]!='B': #체스판의 색깔이 B인데 보드의 색깔이 B가 아니라면
                    count+=1 #count+1
    return count

answer=64 #체스판의 최대 개수는 64개이므로 64로 초기화

for i in range(n-7): #체스판의 크기가 8x8이므로
    for j in range(m-7): #n-7, m-7까지 반복
        answer=min(answer,check(i,j),64-check(i,j)) #체스판의 색깔이 W인 경우와 B인 경우를 모두 고려하여 최소값을 구함
print(answer)
