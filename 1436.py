n=int(input())
num=666 #종말의수
while n>0:
    if '666' in str(num): #666을 문자열로 바꿔서 포함되어있는지 확인
        n-=1 #n이 0이될때까지 반복
    num+=1 #num을 계속 증가시키기. n이 0이될때까지
print(num-1)