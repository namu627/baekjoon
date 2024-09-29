from collections import deque #덱(deque)자료형 사용하려면 import해야함
import sys
N=int(sys.stdin.readline()) #메모리초과 떠가지고 조금이나마 줄여볼라고..
arr=[]
for i in range(N):
    arr.append(i+1) #입력받아주시고
arr=deque(arr) #popleft랑 rotate 쓸거라서 deque으로 형변환
while len(arr)>1: #카드가 한장 남을때까지 반복
    arr.popleft() #popleft하면 맨 왼쪽 요소가 없어짐
    arr.rotate(-1) #rotate(-1)하면 맨 왼쪽 요소가 맨 오른쪽에 추가됨. rotate(1)하면 반대로.
print(arr[0])