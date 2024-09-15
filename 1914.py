def hanoi(x, start, end, via): #하노이 함수(원판갯수, 시작하는 막대, 끝나는 막대, 중간에 거쳐가는 막대)
    if x==1: #원판 1개옮기는 경우
        print(start,end) #시작막대랑 끝나는 막대 출력
        return #종료
    hanoi(x-1, start, via, end) #제일 큰 원판 빼고 위에 있는 원판들을 중간 막대로 옮겨놔야 함
    print(start,end) #시작막대랑 끝나는 막대 출력
    hanoi(x-1, via, end, start) #중간에 옮겨놨던 원판들을 끝나는 막대로 옮겨야 함
def count(x): #횟수 카운트 함수
    if x==1:
        return 1 #1이면 1반환
    else:
        return 2*count(x-1)+1 #횟수 계산 공식이 2*(전항)+1이여서 이렇게 반환
n=int(input())
if n>20: #n이 20보다 크면 횟수만 출력
    print(count(n))
else:
    print(count(n))
    hanoi(n, 1,3,2)