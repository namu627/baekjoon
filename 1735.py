a,b=map(int,input().split())
c,d=map(int,input().split())

e=(a*d+b*c) #분자
f=(b*d) #분모

def gcd(x, y):  #최대공약수
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
g=gcd(e,f) #분자 분모의 최대공약수

print(e//g, f//g)