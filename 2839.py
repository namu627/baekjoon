n=int(input())
ans=[]
for i in range(n//5,-1,-1): #5로 일단 나누고 나머지를 3으로 나눠보면서
    if (n-5*i)%3==0: #맞아 떨어지는게 있으면 리스트에 추가하고
        ans.append(i+(n-5*i)//3)
if not ans: #비어있으면 -1 출력하고
    print(-1)
else:
    print(min(ans)) #아니면 그중에 최소값 출력