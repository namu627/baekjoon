import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:]))
    
    count = 0
    result = -1

    def merge_sort(p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort(p, q)      # 전반부 정렬
            merge_sort(q + 1, r)  # 후반부 정렬
            merge(p, q, r)

    def merge(p, q, r):
        nonlocal count, result
        i, j = p, q + 1
        tmp = []
        
        while i <= q and j <= r:
            if a[i] <= a[j]:
                tmp.append(a[i])
                i += 1
            else:
                tmp.append(a[j])
                j += 1

        while i <= q:
            tmp.append(a[i])
            i += 1
        while j <= r:
            tmp.append(a[j])
            j += 1

        t = 0
        for index in range(p, r + 1):
            a[index] = tmp[t]
            count += 1
            if count == k:
                result = a[index]
            t += 1
    merge_sort(0, n - 1)
    print(result)
solve()