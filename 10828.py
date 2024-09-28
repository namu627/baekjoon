N=int(input())
stack=[]
ans=[]
for _ in range(N):
    order=input().split()
    if order[0]=="push":
        stack.append(order[1])
    elif order[0]=="pop":
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack.pop())
    elif order[0]=="size":
        ans.append(len(stack))
    elif order[0]=="empty":
        if len(stack)==0:
            ans.append(1)
        else:
            ans.append(0)
    elif order[0]=="top":
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
for i in ans:
    print(i)