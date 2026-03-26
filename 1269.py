a,b=map(int,input().split())
a_set=set(map(int,input().split()))
b_set=set(map(int,input().split()))

print(len(list(a_set^b_set))) #^는 두개의 set에서 겹치는 부분을 제외한 나머지를 반환함