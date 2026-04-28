import sys #백준 서비스 종료로 인해 이걸 끝으로 백준은 마무리
input=sys.stdin.readline

def draw_stars(n):
    if n==1:
        return ['*']

    stars=draw_stars(n//3)
    l=[]

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+' '*(n//3)+s)
    for s in stars:
        l.append(s*3)
    return l

n=int(input())
print('\n'.join(draw_stars(n)))