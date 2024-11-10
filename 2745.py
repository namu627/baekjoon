n,b=input().split()
b=int(b)
n=list(n) #입력받은 수를 리스트에 나눠넣고
for i in range(len(n)):
    n[i]=ord(n[i]) #다 아스키코드로 바꾼다음
    if n[i]<58: #숫자인건 숫자 그대로 써야하니 48빼주고 (9가 아스키코드로 57임)
        n[i]-=48
    else: #문자인건 숫자로 바꿈 (Z가 아스키코드로90)
        n[i]-=55
ans=0
for i in range(len(n)):
    ans+=n[i]*(b**(len(n)-1-i)) #진법변환 각 자리 곱하기 진법^(자릿수-1) 해서 다 더하면 됨
print(ans)