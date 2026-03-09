n,m=map(int,input().split())

n_word=[]
m_word=[]
ans=0

for i in range(n):
    n_word.append(input()) #갖고있는 단어 리스트 받기
for i in range(m):
    m_word.append(input()) #확인해야하는 단어 리스트 받기

for i in m_word: #확인해야하는 단어들을
    if i in n_word: #갖고있는 단어리스트안에 있으면 갯수올리기
        ans+=1
print(ans)