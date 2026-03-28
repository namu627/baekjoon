# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n                       n번
#         for j <- 1 to n                   n번
#             for k <- 1 to n               n번
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

n=int(input())
print(n*n*n)
print(3)