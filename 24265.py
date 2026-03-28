# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1      n번 
#         for j <- i + 1 to n    n-1번
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

n=int(input())
print(n*(n-1)//2)
print(2)
