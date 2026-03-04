num=int(input())
line=1

#1/1
#1/2 2/1
#3/1 2/2 1/3
#1/4 2/3 3/2 4/1
#5/1 4/2 3/3 2/4 1/5
#이런식으로 홀수줄의 경우 분자가 1부터 시작해서 증가하고 짝수줄은 분모가 1부터 시작해서 증가하는 패턴이 있음
#그래서 몇번째 줄에 있는지 찾고 그 줄이 홀수인지 짝수인지에 따라 분자와 분모를 구하는 방식으로 풀이

while num>line:
    num=num-line
    line=line+1 #몇번째 줄에 숫자가 있는지

if line%2==1: #line이 홀수인경우
    x=line-num+1 #분자
    y=num #분모
else: #line이 짝수일때
    x=num #분자
    y=line-num+1 #분모

print(f"{x}/{y}")