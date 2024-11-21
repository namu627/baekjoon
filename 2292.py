n=int(input()) #규칙을 찾으면 쉬움. 1+6*n 
ans=1 #이동 거리
bee=1 #이동 거리에 따라 늘어나는 벌집의 수
while True:
    if n>bee:
        bee=bee+(6*ans)
        ans+=1
    else:
        break
print(ans)