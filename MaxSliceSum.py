def solution(A):
    maxSum = curSum = A[0]

    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum

