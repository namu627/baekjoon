from itertools import permutations
n=int(input())
a=input().split()
b=0
max=0
for i in list(permutations(a,n)):
    for j in range(n-1):
        b=b+abs(int(i[j])-int(i[j+1]))
        if b>=max:
             max=b
    b=0
print(max)
