def solution(A):
    """
    A = [1, 3, 6, 4, 1, 2]

    scan seen to find the first missing integer
    seen = [T, T, T, T, F, T, F]

    """
    seen = [False] * (len(A)+ 1)

    for num in A:
        if num > 0 and num <= len(A):
            seen[num-1] = True

    for idx,value in enumerate(seen):
        if not value:
            return idx + 1
    # Numbers are consecutive in A
    # [1,2,3,4] -> return 5
    return len(A) + 1