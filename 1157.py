word=input().upper() #mississipi -> MISSISSIPI
wordlist=list(set(word)) #['S', 'P', 'M', 'I']
arr=[]
for i in wordlist:
    arr.append(word.count(i)) #wordlist에 저장된 알파벳 하나씩 비교하면서 개수세기
if arr.count(max(arr))>1: #제일 많이 나온 알파벳의 갯수가 2개 이상이면
    print("?")
else:
    print(wordlist[arr.index(max(arr))]) #제일 많이나온 알파벳의 인덱스를 통해 wordlist에서 찾아 출력하기