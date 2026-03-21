n=int(input())

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #f(n) = f(n-1) + f(n-2) ,(n>=2) 문제에 나옴
    
print(fibo(n))