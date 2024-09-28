A,B,C=map(int, input().split())
def 분할정복 (A, B, C):
    if B==1:
        return A%C
    elif B%2==1:
        return ((분할정복(A,B//2,C)**2)*A)%C
    elif B%2==0:
        return (분할정복(A,B//2,C)**2)%C
print(분할정복(A,B,C))