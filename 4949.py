while True:
    s=input() #문자열
    stack=[]
    if s==".": #.들어오면 종료
        break
    for i in s:
        if i in "({[": #소중대괄호 여는거 중에 하나 들어오면 해당 괄호 스택에 넣음
            stack.append(i)
        elif i in ")}]": #소중대괄호 닫는거 중에 하나 들어오면 스택에서 가장 마지막에 들어온 괄호와 짝이 맞는지 확인
            if not stack: #스택이 비어있는데 닫는 괄호가 들어오면 짝이 안맞는거
                stack.append(i) #짝이 안맞는거 스택에 넣고
                break #반복문 종료
            if i==")" and stack[-1]=="(": #닫는 괄호가 있고 스택 제일 위에있는게 짝맞는 괄호면 스택에서 제거
                stack.pop()
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            else:
                stack.append(i) #짝이 안맞는거 스택에 넣고
                break
    print("yes" if not stack else "no") #스택이 비어있으면 짝 맞는거, 뭐라도 있으면 짝 안맞는거