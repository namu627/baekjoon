import sys

def cantor(n):
    if n==0:
        return "-"
    
    prev=cantor(n-1)

    return prev + " " * (3**(n - 1)) + prev

for line in sys.stdin:
    try:
        n=int(line)
        print(cantor(n))
    except EOFError:
        break