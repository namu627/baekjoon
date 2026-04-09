import sys
input=sys.stdin.readline

n=int(input())
stack=[]
for _ in range(n):
    order=input().split()
    if order[0]=="1": #정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
        stack.append(order[1])
    elif order[0]=="2": #스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(stack.pop() if stack else "-1")
    elif order[0]=="3": #스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif order[0]=="4": #스택이 비어있으면 1, 아니면 0을 출력한다.
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0]=="5": #스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if not stack:
            print(-1)
        else:
            print(stack[-1])
