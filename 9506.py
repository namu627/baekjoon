while True:
    n=int(input())
    if n==-1: #-1 입력받으면 그만
        break
    num=[]
    for i in range(1,n+1): 
        if n%i==0:
            num.append(i) #약수 다 num에 저장
    if sum(num)==n*2: #약수의 합이 n의 두배면 완전수.
        print(n,'= 1', end='') 
        del num[0] #1이랑 자기 자신은 프린트 안하게 빼고 나머지 반복문으로 프린트
        num.pop()
        for i in num:
            print(' +',i, end='')
        print('')
    else:
        print(n,'is NOT perfect.') #완전수가 아닙니다