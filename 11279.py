import sys
import heapq #heapq를 쓰기 위한 import

N=int(sys.stdin.readline())
X=[] #X숫자 받을 리스트고요
arr=[] #자료형 최대힙 만들 리스트입니다
for _ in range(N):
    X.append(int(sys.stdin.readline()))
for i in X: #X입력받은거 하나식 보면서
    if type(i)==int:
        heapq.heappush(arr,-i)
    elif len(arr)>0 and i==0:
        print(-heapq.heappop(arr))
    else:
        print(0)