n=int(input())
white=[[0 for i in range(100)] for j in range(100)] #100x100 2차원 배열 생성. 흰도화지
for i in range(n):
    x,y=map(int,input().split())
    for j in range(10):
        for k in range(10):
            white[x+j][y+k]=1 #x y 입력받아서 10x10색종이 범위만큼 1넣기
ans=0
for i in range(100): #그냥 count쓰면 못찾길래
    ans+=white[i].count(1) #하나씩 훑으면서 개수 새기
print(ans)