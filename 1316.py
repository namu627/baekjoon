n=int(input())
ans=n
for _ in range(n):
    word=input()
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            ans=ans-1
            break
print(ans)