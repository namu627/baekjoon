n=int(input())
ans=n
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]==word[i+1]: #현재 알파벳과 그다음 알파벳이 일치하면 계속하기
            continue
        elif word[i] in word[i+1:]: #현재 알파벳부터 끝까지 봤을때 똑같은 알파벳이 있으면 반복단어가 아님.
            ans=ans-1
            break
print(ans)