import sys #sys.stdin.readline 쓰려고 import. 입력 빨리받을라고...
n,m=map(int,sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
a.sort() #나무들 길이 정렬해서 이진탐색 할건데
start=1 #start값은 1로 고정하고
end=a[-1] #가장 긴 나무를 end값으로 설정
ans=0 #답 저장할 변수
while start<=end: #start와end가 같거나 start가 end보다 작을경우 반복
    mid=(start+end)//2 #중간값은 start와 end값의 절반
    tree=0 #자르고 남은 나무의 길이 합
    for i in a: 
        if mid<i: #설정한 중간값으로 나무 자를건데 중간값보다 긴 나무 있으면
            tree=tree+(i-mid) #나무 자르고 잘린 나무 길이 더함
    if tree<m: #원하는 나무길이보다 자른 나무가 더 짧으면
        end=mid-1 #절단기 높이를 낮춰야 하니 작은 값 재탐색
    else: #원하는 나무길이보다 자른 나무가 더 길거나 같으면
        ans=mid #답에 절단기 값 저장하고
        start=mid+1 #일단 큰 값으로 재탐색
print(ans)