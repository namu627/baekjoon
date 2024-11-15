arr=[] #2차원 배열이 될 리스트
lenth=[] #각 줄들의 길이를 저장할 리스트
ans='' #최종 출력할 문장
for _ in range(5): #5줄 입력받을거
    a=list(input()) #입력받아서 리스트로 arr에 저장하기(2차원배열)
    lenth.append(len(a)) #n번째줄 길이도 저장해주기
    arr.append(a)
for i in range(max(lenth)): #문장 중에서 가장 긴 문장길이만큼 반복
    for j in range(5): #입력받은게 5줄이니까 5번반복
        if i<lenth[j]: #문장길이가 최대문장길이보다 짧아서 출력할 수가 없다면 빼고 출력해야 하므로 출력할게 있을떄만 ans에 한글자씩 넣기
            ans+=arr[j][i]
print(ans)