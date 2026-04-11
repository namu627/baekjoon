import sys
from collections import deque

input=sys.stdin.readline
queue=deque()

for _ in range(int(input())):
    order=input().split()
    if order[0]=="push": #정수 X를 큐에 넣는 연산이다.
        queue.append(order[1])
    elif order[0]=="pop": #큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(queue.popleft() if queue else -1)
    elif order[0]=="size": #큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    elif order[0]=="empty": #큐가 비어있으면 1, 아니면 0을 출력한다.
        print(0 if queue else 1)
    elif order[0]=="front": #큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(queue[0] if queue else -1)
    elif order[0]=="back": #큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(queue[-1] if queue else -1)
    