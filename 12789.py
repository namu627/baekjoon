import sys
input=sys.stdin.readline

n=int(input())
stack=[]
students=list(map(int, input().split()))
count=1 #순서

for i in students:
    stack.append(i) #일단 학생을 stack에 넣음
    while stack and stack[-1]==count: #stack의 top이 count와 같으면 stack에서 pop하고 count를 1 증가시킴
        stack.pop()
        count+=1

print("Nice" if not stack else "Sad") #stack이 비어있으면 "Nice"를 출력하고, 그렇지 않으면 "Sad"를 출력