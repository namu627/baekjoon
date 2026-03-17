n,k=map(int,input().split())
#이항계수 공식: nCk=n!/(k!*(n-k)!)
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(n)//(factorial(k)*factorial(n-k)))