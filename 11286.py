apb=[-1]*26 #알파벳 26글자
s=list(input())
for i in range(len(s)):
    if apb[ord(s[i])-97]==-1:
        apb[ord(s[i])-97]=i
print(apb)