grade_list=['A+','A0','B+','B0','C+','C0','D+','D0','F'] #등급 리스트. 인덱스로 호출할거임
score=[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0] #등급별 점수 리스트
a=b=0 #a는 학점*과목평점의 합이고 b는 학점의 총합을 저장할 변수이다
for i in range(20):
    subject,credit,grade=input().split() #과목명 / 학점 / 등급
    credit=float(credit)
    if grade=='P': #등급이 P면 계산안할거임. 그래서 얘만 따로 if문으로 빼고 나머지계산을 else로 넣기
        continue
    else:
        a+=credit*score[grade_list.index(grade)] #학점*과목평점 의 합
        b+=credit #학점총합
print(round(a/b,6)) #전공평점은 (학점*과목평점)의 총합 / 학점총합 이기때문