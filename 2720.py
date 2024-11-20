t=int(input())
for _ in range(t):
    arr=[]
    c=int(input()) #돈 입력받고
    arr.append(c//25) #25원으로 나눈 몫 저장하고 나머지로 재계산하기 반복
    c=c%25
    arr.append(c//10)
    c=c%10
    arr.append(c//5)
    c=c%5
    arr.append(c//1)
    print(*arr)