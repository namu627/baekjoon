import sys
from collections import deque

input=sys.stdin.readline
deck=deque()

for _ in range(int(input())):
    order=input().split()
    if order[0]=="1": #정수 X를 덱의 앞에 넣는다.
        deck.appendleft(order[1])
    elif order[0]=="2": #정수 X를 덱의 뒤에 넣는다.
        deck.append(order[1])
    elif order[0]=="3": #덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(deck.popleft() if deck else -1)
    elif order[0]=="4": #덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(deck.pop() if deck else -1)
    elif order[0]=="5": #덱에 들어있는 정수의 개수를 출력한다.
        print(len(deck))
    elif order[0]=="6": #덱이 비어있으면 1, 아니면 0을 출력한다.
        print(1 if not deck else 0)
    elif order[0]=="7": #덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        print(deck[0] if deck else -1)
    elif order[0]=="8": #덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        print(deck[-1] if deck else -1)

