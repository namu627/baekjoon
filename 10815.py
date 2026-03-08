n=int(input()) #갖고있는 숫자카드수
n_card=set(map(int,input().split())) #갖고있는 숫자카드 세트(리스트로 하면 시간초과남)
m=int(input()) #확인해야할 카드수
m_card=list(map(int,input().split())) #확인해야할 카드 리스트

for i in m_card: #확인해야 할 카드 리스트 보면서
    if i in n_card: #갖고있는 카드 리스트에 있으면
        print(1,end=' ') #1 출력
    else:
        print(0,end=' ') #아니면 0출력