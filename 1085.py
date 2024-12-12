x,y,w,h=map(int,input().split())
arr=[x,w-x,y,h-y] #min함수를 쓰면 최소값을 찾기 쉬우므로 리스트 만들어서 넣기
print(min(arr))