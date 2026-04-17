import sys
input=sys.stdin.readline

rainbowdance={"ChongChong"} #레인보우 댄스 추는사람. 중복추가 없애기 위해서 set사용

for _ in range(int(input())):
    a,b=input().split()

    if a in rainbowdance or b in rainbowdance: #둘중 한명이라도 춤추고있으면 나머지 한명도 댄스 set에 추가하기
        rainbowdance.add(a)
        rainbowdance.add(b)

print(len(rainbowdance))