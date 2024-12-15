from itertools import permutations #순열과 조합을 쓰기위한 임포트
n,m=map(int,input().split())
card=list(map(int,input().split())) #n장의 카드들
ans=[]
for i in permutations(card,3): #n장의 카드들중에 m개의 카드를 뽑아서 조합하고
    if sum(i)<=m: #그 합이 m보다 작거나 같으면 ans에 저장
        ans.append(sum(i))
print(max(ans)) #그리고 저장된 값중 가장 큰값을 답으로 출력