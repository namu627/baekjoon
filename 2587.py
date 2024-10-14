arr=[]
for _ in range(5):
    arr.append(int(input()))
arr.sort()
avg=0
for i in range(5):
    avg+=arr[i]
avg=avg//5
print(avg)
print(arr[2])