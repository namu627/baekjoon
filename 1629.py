A,B,C=map(int, input().split())
def 분할정복 (A, B, C): #(A**B)%C를 구할건데 분할정복을 사용할것임.
    if B==1: #B가 1이면 그냥 A를 C로 나눈 나머지 구하면 됨
        return A%C
    elif B%2==1: #B가 홀수면 B를 반으로 쪼개도 A를 한번 더 곱해줘야 하니까 (지수법칙)
        return ((분할정복(A,B//2,C)**2)*A)%C #B반으로 나눠서 재귀 한번 돌리고 다시 2제곱 해주고 A한번 더 곱해주고 C로 나눈 나머지 구하기
    elif B%2==0: #B가 짝수면 B를 반으로 쪼개서 분할정복 하면 됨
        return (분할정복(A,B//2,C)**2)%C #B를 반으로 나눠서 재귀 한번 돌리고 2제곱 해주고 C로 나눈 나머지 구하기
print(분할정복(A,B,C))