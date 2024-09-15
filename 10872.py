def f(x): #팩토리얼 함수 정의
    if x==1 or x==0: #f(1)일때 또는 0팩토리얼은 1이므로
        return 1 #1을 반환
    else: #f(1)이 아닐때 
        return x*f(x-1) #현재 x값에 하나 f(x-1) 리턴값을 곱한 값을 반환. 결국 1까지 갔다가 돌아오면서 곱해짐
n=int(input())
print(f(n))