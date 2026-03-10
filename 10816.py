import sys

#입력을 더 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

n=int(input())
n_card=list(map(int, input().split()))
m=int(input())
m_card=list(map(int, input().split()))

count_dict = {}

for card in n_card:
    if card in count_dict:
        count_dict[card] += 1  #n_card 리스트에서 i의 개수를 세어서 ans 리스트에 추가
    else:
        count_dict[card] = 1

ans = []
for i in m_card:
    #dict.get(key, default)를 사용하면 key가 없을 때 0을 반환함
    ans.append(count_dict.get(i, 0))

print(*ans)

