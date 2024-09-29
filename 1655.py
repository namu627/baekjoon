import sys
from heapq import heappop, heappush
N=int(sys.stdin.readline())
maxheap=[] #최대힙은 뿌리노드가 가장 큰 값이고 최소힙은 뿌리노드가 가장 작은 값이므로
minheap=[] #큰값들은 최소힙에 작은값들은 최대힙에 저장해서(반 나눠서 큰수중에 가장 작은값과 작은수중에 가장 큰 값 비교) 뿌리노드만 비교해 중간값 찾기
ans=[] #답 저장할 리스트
for i in range(N):
    if len(maxheap) == len(minheap): #만약 최소힙과 최대힙에 똑같이 들어있으면 최대 힙에 저장하기
        heappush(maxheap, -int(sys.stdin.readline())) #heapq는 기본적으로 최소힙이므로 -붙여서 저장하므로써 최대힙으로 만들기
    else:
        heappush(minheap, int(sys.stdin.readline())) #최대힙에 하나 넣었으면 최소힙에 하나 넣기

    if minheap and -maxheap[0] > minheap[0]: #각각 수를 넣었을때 최대힙 최솟값이 최소힙 최대값보다 클경우에 두개 바꿔서 넣기(큰수 작은수 정확히 반으로 나누기 위함)
        temp_min=heappop(minheap)
        temp_max=heappop(maxheap)
        heappush(maxheap,-temp_min)
        heappush(minheap,-temp_max)
    ans.append(-1*maxheap[0]) #짝수개면 두수중에 작은 수 출력해야 하고, 홀수인경우엔 최대힙에 숫자가 항상 하나 더 많으니 최대힙 뿌리노드값을 답에 저장(-붙여놨기때문에 음수 붙여서)
for i in ans:
    print(i)