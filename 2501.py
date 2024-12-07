n,k=map(int,input().split())
count=0 #약수 개수
for i in range(1,n+1):
    if n%i==0: #약수이면 개수 카운트 +1
        count+=1
        if count==k: #k번째 약수이면 프린트
            print(i)
if count<k: #약수의 개수가 k개보다 적으면 0 프린트
    print(0)