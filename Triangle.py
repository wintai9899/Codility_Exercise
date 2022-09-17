def solution(A):
    A.sort()
    if len(A) < 3:
        return 0
    # comparing triplets
    for i in range(len(A) - 2):
        if A[i] > 0 and A[i] + A[i+1] > A[i + 2]:
            return 1

    return 0