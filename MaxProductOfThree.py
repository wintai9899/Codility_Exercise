def solution(A):
    """
    A = [-3,1,2,-2,5,6]

    nums = [-3,-2,1,2,5,6]
    """
    A.sort()
    N = len(A)
    # smallest 2 negative numbers * largest number
    p1 = A[0] * A[1] * A[N-1]
    # 3 largest positive values in A
    p2 = A[N-1] * A[N-2] * A[N-3]

    return max(p1,p2)