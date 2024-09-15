import sys
# def sort(list): #퀵 정렬을 사용할 것임
#     if len(list)<=1: #리스트 길이가 1보다 작거나 같으면 그대로 반환
#         return list
#     pivot=list[len(list)//2] #중간값 설정
#     a=[] #pivot 보다 작은숫자
#     b=[] #pivot 이랑 같은 숫자
#     c=[] #pivot 보다 큰숫자
#     for i in list:
#         if i>pivot: #중간값보다 크면
#             c.append(i) #리스트 c에 넣기
#         elif i<pivot: #중간값보다 작으면
#             a.append(i) #리스트 a에 넣기
#         elif i==pivot: #중간값이랑 동일하면
#             b.append(i) #리스트 b에 넣기
#     return sort(a)+b+sort(c) #같은값은 놔두고 작은값 큰값 다시 함수에 넣어서 리스트 합쳐서 반환하기
n=int(sys.stdin.readline())
x=[]
for i in range(n):
    x.append(int(sys.stdin.readline()))
x.sort()
for j in x:
    print(j)