import math
n=int(input())

tree=[] #가로수
for _ in range(n):
    tree.append(int(input()))

간격=[]
for i in range(1, len(tree)):
   간격.append(tree[i]-tree[i-1]) #가로수 사이 간격을 리스트로 저장

최대공약수=math.gcd(*간격) #가로수 간 간격들의 최대공약수를 구함

for i in range(len(간격)): #각 간격을 최대공약수로 나눔
   간격[i]=간격[i]//최대공약수

print(sum(간격)-len(간격)) #각 간격을 최대공약수로 나눈 값들의 합에서 간격의 개수를 빼면 필요한 가로수의 개수가 나옴