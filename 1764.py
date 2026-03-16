n,m=map(int,input().split())
<<<<<<< HEAD
n_list=[]
for i in range(n):
    n_list.append(input())

=======
듣=set(input() for _ in range(n))
보=set(input() for _ in range(m))
듣보=[]
for i in 듣: #듣지도 못한 사람중에
    if i in 보: #보지도 못한 사람이 있으면
        듣보.append(i) #듣보잡에 추가

print(len(듣보))
for i in sorted(듣보): #사전순으로 정렬해서 출력
    print(i)
>>>>>>> 9175fd09614d6b5d4502b02aeaef7f7443859c3f
