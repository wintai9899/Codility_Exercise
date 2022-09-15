def solution(A, K):
    if not A:
        return []

    K = K % len(A)
    # 1. Reverse entire array
    reverse_Arr(A, 0, len(A) - 1)

    # 2. Reverse A[:k-1]
    reverse_Arr(A, 0, K - 1)

    # 3. Reverse A[K:]
    reverse_Arr(A, K, len(A) - 1)

    return A


def reverse_Arr(A, start, end):
    if not A:
        return
    while start <= end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

    return A