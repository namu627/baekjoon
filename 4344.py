c = int(input()) #케이스 개수 받음
av = 0
b = 0
x= []
for i in range(c): #케이스 개수만큼 반복
    a = list(input().split())
    for j in range(int(a[0])):
        av = av+int(a[j+1])
    av = av/int(a[0])
    for j in range(int(a[0])):
        if int(a[j+1]) > av:
            b = b+1
    x.append(round(b*100/int(a[0]),3))
    av=0
    b=0
for i in range(c):
    print(x[i],"%",sep='') #sep 쓰면 공백없이 출력됨
