import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
list=[]

for i in range(n):
    list.append(int(input()))

print(round(sum(list)/n)) #산술평균
list.sort()
print(list[n//2]) #중앙값

cnt=Counter(list).most_common() 
if len(cnt) > 1:
    max_freq=cnt[0][1]
    modes=[val for val, freq in cnt if freq==max_freq]
    
    if len(modes) > 1:
        print(modes[1])
    else:
        print(modes[0])
else:
    print(cnt[0][0])

print(list[-1]-list[0]) #범위