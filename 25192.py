import sys
input = sys.stdin.readline

n=int(input())

gomgom=0
chat_set=set() #set으로 중복제거할생각

for _ in range(n):
    chat=input().strip()
    
    if chat=="ENTER": #ENTER가 나오면 gomgom에 지금까지의 채팅방에 있던 사람 수를 더해주고 chat_set을 초기화
        gomgom+=len(chat_set)
        chat_set.clear() 
    else:
        chat_set.add(chat)

gomgom+=len(chat_set) #마지막에 ENTER가 나오지않고 끝나는 경우도 있기때문에 마지막에 chat_set의 길이를 더함
print(gomgom)