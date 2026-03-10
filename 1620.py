import sys
input = sys.stdin.readline

n,m=map(int,input().split())
pokemon_num=[] #포켓몬도감
pokemon_name={}

for i in range(n):
    name=input().rstrip()
    pokemon_num.append(name)
    pokemon_name[name]=i+1
quiz=[]
for i in range(m):
    quiz.append(input().rstrip())
for i in quiz:
    if i.isdigit(): #문자열이 숫자로만 이루어져 있는지 확인하는 isdigit사용
        print(pokemon_num[int(i)-1]) #문자열을 정수로 변환하여 포켓몬 번호에 해당하는 이름 출력
    else:
        print(pokemon_name[i]) #문자열이 숫자가 아니면 포켓몬 이름에 해당하는 번호 출력