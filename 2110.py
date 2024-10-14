h,m=map(int, input().split())
if h==0:
    h+=24
if m<45:
    h-=1
    m+=60
print(h,m-45)