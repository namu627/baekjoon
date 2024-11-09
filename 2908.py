a,b=input().split()
a=int(a[::-1]) #[::-1]하면 문자열 뒤집기임. 문자열[시작:끝:규칙]이라서 -1이면 뒤에서부터 한글자씩이라는 뜻
b=int(b[::-1]) 
if a>b:
    print(a)
else:
    print(b)