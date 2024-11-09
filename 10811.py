n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(i+1)
a=[] #임시저장해서 뒤집을 리스트
for x in range(m):
    i,j=map(int,input().split())
    a=arr[i-1:j] #i부터j까지 잘라서 임시리스트에 넣고
    a.reverse() #뒤집은다음에
    arr[i-1:j]=a #다시 바꿔넣기
print(*arr)