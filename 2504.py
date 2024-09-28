def cal(str):
    stack=[]
    score=0
    for i in range(len(list(str))):
        stack.append(str[i])
        if len(stack)==1 and type(stack[0])==int:
            print(stack[0])
            return
        elif len(stack)>=2 and stack[-2]=="(" and stack[-1]==")": #앞에 들어온것중에 왼쪽괄호가 있고 이번에 들어온게 오른쪽 괄호면
            stack.pop()
            stack.pop()
            stack.append(2)
        elif len(stack)>=2 and stack[-2]=="[" and stack[-1]=="]": #앞에 들어온것중에 왼쪽괄호가 있고 이번에 들어온게 오른쪽 괄호면
            stack.pop()
            stack.pop()
            stack.append(3)
        elif len(stack)>=3 and stack[-3]=="(" and stack[-1]==")" and type(stack[-2])==int:
            stack.pop(-3)
            stack.pop()
            stack[-1]=int(stack[-1])*2
        elif len(stack)>=3 and stack[-3]=="[" and stack[-1]=="]" and type(stack[-2])==int:
            stack.pop(-3)
            stack.pop()
            stack[-1]=int(stack[-1])*3
        elif len(stack)>=2 and type(stack[-1])==int and type(stack[-2])==int:
            stack[-2]=stack[-2]+stack[-1]
            stack.pop()
    cal(stack)
def VPS(str): #VPS인지 판별하는 함수. PS는 문자열
    stack=[] #스택하나 만들어주고
    for i in list(str): #PS문자열을 리스트에 한문자씩 넣어서 볼거임
        stack.append(i) #스택에 일단 하나씩 넣어주다가
        if len(stack)>=2 and stack[-2]=="(" and stack[-1]==")": #앞에 들어온것중에 왼쪽괄호가 있고 이번에 들어온게 오른쪽 괄호면
            stack.pop() #오른쪽 괄호 빼고
            stack.pop() #전에 들어온 왼쪽 괄호도 뺌
        if len(stack)>=2 and stack[-2]=="[" and stack[-1]=="]": #앞에 들어온것중에 왼쪽괄호가 있고 이번에 들어온게 오른쪽 괄호면
            stack.pop() #오른쪽 괄호 빼고
            stack.pop() #전에 들어온 왼쪽 괄호도 뺌
    if len(stack)==0: #다 하고나서 마지막에 스택에 뭐가 안남아있으면 VPS인거니까 YES출력하고 끝냄
        cal(str)
        return
    else:
        print(0)
        return
str=input()
VPS(str)