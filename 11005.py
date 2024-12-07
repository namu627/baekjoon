n,b=map(int,input().split())
arr=[] #답 저장할 리스트
while True:
    if n<b: #더이상 나눌수 없으면 몫 추가하고 종료
        arr.insert(0,n) #리스트 앞에 추가하려면 append말고 insert사용해야함
        break
    arr.insert(0,n%b) #나눈 나머지 저장하고 
    n=n//b #나눈 후 다시 반복
for i in range(len(arr)): 
    if arr[i]>9: #숫자로 표현 못할경우
        arr[i]=chr(arr[i]+55) #아스키코드를 이용해 문자로 변환. Z가 90이기 때문에 55 더해주는 거임
for i in arr:
    print(i,end='')