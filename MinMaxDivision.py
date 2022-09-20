def solution(K, M, A):
    blocksNeeded = 0

    lowerBound = max(A)
    upperBound = sum(A)

    res = 0
    # divide into only 1 block
    if K == 1:
        return upperBound
    # blocks number > len(A)
    if K >= len(A):
        return lowerBound

    while lowerBound <= upperBound:
        mid = (lowerBound + upperBound) // 2

        blocksNeeded = blocksNumber(A, mid)

        if blocksNeeded <= K:
            upperBound = mid - 1
            res = mid
        else:
            lowerBound = mid + 1

    return res

def blocksNumber(A, maxBlock):
    blockNumber = 1

    preBlockSum = A[0]

    for element in A[1:]:
        if preBlockSum + element > maxBlock:
            preBlockSum = element
            blockNumber += 1

        else:
            preBlockSum += element
    return blockNumber