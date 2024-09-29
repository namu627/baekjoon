N,K=map(int,input().split())
arr=[] #숫자 저장
ans=[] #답 저장 리스트
for i in range(N):
    arr.append(i+1) #1부터 N까지 리스트 만듦
i=1
while len(ans)!=N: #N개의 숫자가 모두 뽑히면 중단
    if i%K==0: #K번째 숫자는 뽑아야됨
        ans.append(arr[i-1]) #답 저장 리스트에 추가하기
        i=i+1
    else: #그렇지 않은 숫자들은 arr뒤에 추가해서 다시뽑기
        arr.append(arr[i-1])
        i=i+1
print('<',end='') #end=''하면 띄어쓰기 없이 출력된다
for i in range(N-1):
    print(ans[i],end=', ')
print(ans[N-1], end='')
print('>',end='')