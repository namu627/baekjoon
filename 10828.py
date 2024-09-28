N=int(input())
stack=[] #스택 구현할 리스트
ans=[] #답 저장할 리스트
for _ in range(N): #명령어 N번 받을거라
    order=input().split() #명령어를 order라는 리스트에 입력받아서 인덱스 0번째로 판단해서 명령어 실행할 것임
    if order[0]=="push": 
        stack.append(order[1]) #push 명령어 뒤에있는 숫자를 스택에 추가. 참고로 append()하면 리스트 맨 뒤에 추가된다
    elif order[0]=="pop":
        if len(stack)==0: #스택이 비어있을경우는 -1을 출력값에 저장
            ans.append(-1)
        else:
            ans.append(stack.pop()) #pop()은 리스트의 맨 뒤값을 없애고 반환한다. stack의 맨 뒤값 제거하고 출력값에 추가
    elif order[0]=="size":
        ans.append(len(stack)) #스택 길이
    elif order[0]=="empty":
        if len(stack)==0: #스택 비어있으면 1값을 출력값에 추가
            ans.append(1)
        else:
            ans.append(0) #아니면 0값 추가
    elif order[0]=="top":
        if len(stack)==0: #스택 비어있으면 -1값 출력하고
            ans.append(-1)
        else:
            ans.append(stack[-1]) #아니면 스택 맨 뒷값 출력값에 저장
for i in ans:
    print(i)