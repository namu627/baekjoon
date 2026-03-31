def gcd(x, y):  #최대공약수
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
  
def lcm(x, y):  #최소공배수
  result=(x*y)//gcd(x,y)
  return result

#유클리드 호제법: 두 수의 곱/최대공약수=최소공배수
a,b=map(int, input().split())
print(lcm(a,b))