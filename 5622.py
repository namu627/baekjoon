arr=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #리스트로 만들어놓고
s=list(input())
ans=0
for i in range(len(s)):
    for j in arr:
        if s[i] in j: #입력받은 문자 하나씩 보면서 다이얼 리스트 몇번째에 있는지 보다가 있으면
            ans=ans+arr.index(j)+3 #답에 인덱스 번호 더해주고 다이얼이 2칸, 인덱스 1칸 해서 총 3 더해준다
print(ans)