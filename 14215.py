a,b,c=map(int, input().split())
arr=[a,b,c]
if max(arr)>=sum(arr)-max(arr): #만약 삼각형이 안만들어지는 상황이라면
    arr.remove(max(arr)) #젤 긴 막대 뺴고
    arr.append(sum(arr)-1) #길이 맘대로 줄일수 있으니까 길이를 짧은막대 두개 길이 합 보다 1 작게 설정
print(sum(arr))