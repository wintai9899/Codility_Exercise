def solution(A):
    leftSum = A[0]
    rightSum = sum(A) - leftSum

    diff = abs(leftSum - rightSum)

    for p in range(1, len(A)-1):
        leftSum += A[p]
        rightSum -= A[p]

        currentDiff = abs(leftSum - rightSum)

        if currentDiff < diff:
            diff = currentDiff

    return diff