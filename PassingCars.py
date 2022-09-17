def solution(A):
    """
    A = [0, 1, 0, 1, 1]

    suffixSum = [3, 3, 2, 2, 1, 0]

    zeroIdxInA = 0, 2

    res = suffixSum[0] + suffixSum[2] = 3 + 2 = 5
    """
    suffixSum = [0] * (len(A) + 1)
    count = 0
    res = 0
    # loop from the back to calculate suffix sum
    for i in range(len(A) - 1, -1, -1):
        count += A[i]
        suffixSum[i] = count

    for i in range(len(A)):
        if not A[i]:
            res += suffixSum[i]

    return res if res <= 1000000000 else -1

