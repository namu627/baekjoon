s=input()
list=[]

for i in range(len(s)):
    for j in range(i, len(s)):
        list.append(s[i:j+1]) #문자로 만들수있는 모든 조합

print(len(set(list))) #set으로 중복제거, set의 길이 출력하기