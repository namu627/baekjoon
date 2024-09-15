case=int(input()) #테스트 케이스 수
ans=[] #답들을 보관해놓기 위한 리스트
for i in range (case): #테스트 케이스 만큼 반복
    a=list(input()) #이렇게 하면 리스트에 한글자씩 들어감
    finalscore=0 #최종점수
    score=0 #점수(연속으로 맞추면 1점씩 늘어남)
    for j in a: #for문에 숫자 안쓰고 리스트 넣어도 반복이 됨
        if j=='O': #O일경우
            score=score+1 #받는 점수를 1점씩 늘려서
            finalscore=finalscore+score #최종 점수에 합산
        elif j=='X': #X일경우
            score=0 #받는 점수를 0으로 초기화
    ans.append(finalscore) #출력할 답들을 ans 리스트에 추가해놓기
for i in range(case):
    print(ans[i])
