#마지막 좌표는 홀수번 나온 숫자들 조합이므로
x=[] #x좌표만 따로넣고
y=[] #y좌표만 따로넣어서 계산
for _ in range(3): 
    a,b=map(int,input().split())
    if a in x: #x좌표 리스트에 똑같은 값이 있으면 삭제
        x.remove(a)
    else: #아니면 좌표 추가
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
print(*x,*y)