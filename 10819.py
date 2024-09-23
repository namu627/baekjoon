from itertools import permutations #이거 해야지 permutation 쓸 수있음
n=int(input())
a=input().split() #띄어쓰기로 구분해서 a리스트에 하나씩 넣기
b=0 
max=0
for i in list(permutations(a,n)): #순서를 고려해서 a에서 n개 중에 n개를 뽑아 나열함. 그걸 튜플로 만들어줘서 리스트로 형변환
    for j in range(n-1): #각 순열 조합마다 계산할건데 0부터 n-1까지 반복하면서 계산해줌. 왜냐면 마지막 항이 n-1항에서 n항 뺴는거기때문
        b=b+abs(int(i[j])-int(i[j+1])) #변수b를 이용해서 계산식
        if b>=max: #max값보다 현재 조합 계산결과가 더 크면 최대값을 바꿔줄거
             max=b
    b=0
print(max)