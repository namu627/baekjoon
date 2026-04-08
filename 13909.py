# import sys
# n=int(sys.stdin.readline())
# window=[0 for _ in range(n)] #0은 닫힌창문, 1은 열린창문

# for i in range(1, n+1):
#     for j in range(i, n+1, i):
#         if window[j-1]==0: #창문이 닫혀있으면
#             window[j-1]=1 #열고
#         else: #창문이 열려있으면
#             window[j-1]=0 #닫음

# print(sum(window)) #열려있는 창문의 수=1의 개수

#메모리초과 사유: n의 범위가 최대 21억

n=int(input())
print(int(n**0.5)) #열려있는 창문의 수=1의 개수=제곱수의 개수=루트n 이하의 정수의 개수랑 같음