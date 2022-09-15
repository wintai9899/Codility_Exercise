def solution(A):

    sortedArr = A
    sortedArr.sort() 

    # must start from 1
    if sortedArr[0] != 1:
        return 0 

    for i in range(1, len(A)):
        # compare pairs of elements, if diff > 1 means its no consecutive
        if A[i] - A[i-1] != 1:
            return 0 

    return 1