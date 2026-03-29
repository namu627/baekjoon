# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2                             #n-2번 반복
#         for j <- i + 1 to n - 1                     #n-1번 반복
#             for k <- j + 1 to n                     #n번 반복
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

#시간복잡도는 O(n^3)
n=int(input())
print(n*(n-1)*(n-2)//6) #nC3 = n!/(3!(n-3)!) = n(n-1)(n-2)/6
print(3)