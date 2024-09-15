n,x = input().split() #입력받은걸 나눠서 각각 하나씩 할당
n = int(n)
x = int(x)
a = list(input().split()) #입력받은걸 나눠서 리스트에 하나씩 넣음
b = [] 
for i in range(n): #i가 0~n까지 반복
    if int(a[i]) < x: #비교하는데 x값보다 작은게 있으면
        b.append(a[i]) #b에다가 넣음
print(*b) #별 붙이면 리스트 요소 대괄호 없이 출력 가능