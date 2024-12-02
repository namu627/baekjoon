#에라토스테네스의 체 사용하기
m=int(input())
n=int(input())
arr=[0]*(n+1) #1부터 n까지의 수 중에서 소수만 찾아낼것. 0은 소수 표시이고 1은 아니라는 표시
arr[0]=1 #1은 소수가 아니므로 1로 표시
arr[1]=1 #2도 소수가 아니므로 1로 표시
for i in range(2,n+1): #2부터 n까지 돌면서
    if arr[i]==0: #i가 0(소수이거나 확인이 안된 수)이면
        j=2 #현재 수에서 배수들을 다 제외
        while (i*j)<=n: #n 범위 내에서 현재 수의 배수들을 소수에서 제외
            arr[i*j]=1
            j+=1 #배수 늘려가기
ans1=0 #소수들의 합을 저장할 변수
ans2=0 #최소값을 저장할 변수
for i in range(m,n+1): #m부터 n까지 수 중에 소수가 보이면 각 변수에 저장
    if arr[i]==0:
        if ans2==0:
            ans2=i
        ans1+=i
if ans1==ans2==0:
    print(-1)
else:
    print(ans1)
    print(ans2)