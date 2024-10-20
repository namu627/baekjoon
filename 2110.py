import sys
input=sys.stdin.readline

n,c=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start=1 #집이 최소 두개고 같을수 없으니 최소 거리는 1
end=arr[-1]-arr[0] #초기값은 첫집과 마지막집 사이의 거리
ans=0 #답; 최대 공유기 거리

while start<=end: #start값이 end값보다 커지면 종료
    mid=(start+end)//2 #현재 공유기 거리
    home=arr[0] #현재 집. 한개는 무조건 처음 집에 설치할것
    wifi=1 #공유기 설치한 개수
    for i in range(1, n):
        if arr[i]>=home+mid: #현재 집에서 설정한 공유기 거리만큼 더했을때 그 이상의 거리에 있는 집이 있으면 공유기 하나 더 설치
            home=arr[i] #공유기 설치했으니까 현재 집 옮겨주고
            wifi=wifi+1 #공유기 설치했으니까 설치한 개수 하나 더해주고
    if wifi>=c: #설치한 공유기 수가 원하는 공유기 수와 같거나 그거보다 크면
        start=mid+1 #start값을 mid+1값으로 바꿔서 재탐색; 다른 값이 나올수도 있으니
        ans=mid #현재 공유기 거리를 답에 저장
    else: #설치한 공유기 수가 원하는 공유기 수보다 작으면
        end=mid-1 #거리를 좁혀서 재탐색
print(ans)