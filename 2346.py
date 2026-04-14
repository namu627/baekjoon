from collections import deque

n=int(input()) #5
deck=deque(enumerate(map(int, input().split()), 1)) #(풍선 번호, 종이에 적힌 값) 형태로 저장
#([(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)])
result=[]

while deck:
    balloon,paper= deck.popleft() #1, 3
    result.append(balloon)
    
    #풍선이 더 이상 없으면 중단
    if not deck:
        break

    #popleft()로 꺼낸 풍선의 종이에 적힌 값이 양수면 왼쪽으로, 음수면 오른쪽으로 이동
    if paper > 0:
        deck.rotate(-(paper - 1)) #왼쪽으로 이동할 때는 popleft()로 꺼낸 풍선의 종이에 적힌 값에서 1을 뺀 만큼 이동
    else:
        deck.rotate(-paper) #오른쪽으로 이동할 때는 popleft()로 꺼낸 풍선의 종이에 적힌 값의 절댓값 만큼 이동

print(*(result))