n,b=map(int,input().split())
arr=[]
while True:
    if n<b:
        arr.append(n)
        break
    arr.append(n%b)
    n=n//b
for i in range(len(arr)):
    if arr[i]>9:
        arr[i]=chr(arr[i]+55)
for i in arr:
    print(i,end='')