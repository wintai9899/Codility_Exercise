def solution(A):
    """
    Using 2 pointers

    Ideal : abs[A[l]] - abs[A[r]] approx 0. two numbers are very close eg. -3 and 2 -> abssum of 1
    :param A:
    :return:
    """
    A.sort()
    minSum = float("inf")
    l = 0
    r = len(A) - 1

    while l <= r:
        absSum = abs(A[l] + A[r])
        minSum = min(minSum, absSum)

        if abs(A[l]) > abs(A[r]):
            l += 1

        else:
            r -= 1

    return minSum