from itertools import combinations #조합(combination) 내장함수를 쓰려면 해야함
a=[]
for i in range(9):
    a.append(int(input()))
for i in list(combinations(a,7)): #combinations 함수는 a리스트 원소들중 7개로 만들수 있는 조합을 반환해준다. 튜플로 반환해주기 때문에 list 로 형변환
    if sum(i)==100: #9개중에 7개 뽑았는데 원소들의 합이 100이면
        i=list(i) #sort함수 쓰기 위해 튜플->리스트로 형변환
        i.sort() #정렬하고 프린트
        for j in range(7):
            print(i[j])
        break