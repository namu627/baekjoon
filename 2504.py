str=list(input())
stack=[] #문자열 읽으면서 괄호가 닫히는지 확인할 스택
a=1 #계산을 진행할 변수
b=0 #답을 저장할 변수
for i in range(len(str)):
    if str[i]=='(': #소괄호 시작하면
        stack.append(str[i]) #스택에 추가하고
        a=a*2 #2곱하기 (분배법칙으로 계산할거라서 이런식으로 계산)
    elif str[i]=='[': #대괄호 시작하면
        stack.append(str[i]) #추가하고
        a=a*3 #3곱하기(이것도 분배법칙이라 곱해도 계산가능)
    elif str[i]==')': #소괄호 닫힐라고 하면 닫힐수있는지 조건확인
        if not stack or stack[-1]=='[': #스택이 비어있거나 대괄호가 안닫혔는데 소괄호를 닫으려고 하면 완전한 문자열이 아니므로
            b=0 #답은 0 하고 중단
            break
        if str[i-1]=='(': #만약 소괄호 안닫혔으면
            b=b+a #답에 계산한값 저장하고
        stack.pop() #소괄호 닫혔으니 저장된 왼쪽소괄호 스택에서 제거
        a=a//2 #그리고 2로 나눠주기(계속 계산해야 해서.)
    elif str[i]==']': #대괄호 닫을라고 하면 조건확인
        if not stack or stack[-1]=='(': #위랑 동일
            b=0
            break
        if str[i-1]=='[':
            b=b+a
        stack.pop()
        a=a//3
if stack: #계산 다끝났는데 스택에 뭐가 남아있으면(괄호가 안닫힌게 있으면)
    b=0 #답은 0
print(b)