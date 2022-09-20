def solution(A):
    n = len(A)
    d = {}
    lv = lk = 0
    for i in range(len(A)):
        d[A[i]] = d.get(A[i], 0) + 1

        if lv < d[A[i]]:
            lv = d[A[i]]
            lk = A[i]
    if lv <= n / 2:
        return 0
    left = 0
    right = lv
    count = 0
    for i in range(n):
        if A[i] == lk:
            left += 1
            right -= 1
        if left > (i + 1) / 2 and right > (n - i - 1) / 2:
            count += 1
    return count