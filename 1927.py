import sys
import heapq #heapq를 쓰기 위한 import

N=int(sys.stdin.readline())
X=[] #X숫자 받을 리스트고요
arr=[] #자료형 최대힙 만들 리스트입니다
for _ in range(N):
    X.append(int(sys.stdin.readline()))
for i in X: #X입력받은거 하나식 보면서
    if type(i)==int and i!=0: #0이 아니고 자연수이면 최소힙으로 넣어줄것
        heapq.heappush(arr,i) #heapq.heappush(리스트, 값). 값을 힙 정렬하면서 리스트로 push 해줌. 기본이 최소힙
    elif arr and i==0: #힙에 뭔가 들어있고 0이면 값 출력하고 값을 없앨것
        print(heapq.heappop(arr)) #heapq.heappop(리스트)하면 힙 정렬된거에서 가장 작은값을 pop()해준다. 
    else:
        print(0) #아무것도 없으면 0출력