a,b,c,d,e,f=map(int,input().split())
#연립방정식 행렬곱으로 풀기
분모=(a*e-b*d)
x=(e*c//분모)-(b*f//분모)
y=(a*f//분모)-(c*d//분모)
#abcdef로 역행렬 계산식 풀어쓰면 이렇게됨
print(x,y)