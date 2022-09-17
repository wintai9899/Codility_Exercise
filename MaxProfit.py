def solution(A):
    l = 0
    maxProfit = 0

    for r in range(len(A)):
        if A[r] > A[l]:
            profit = A[r] - A[l]
            maxProfit = max(maxProfit, profit)

        else:
            l = r

    return maxProfit