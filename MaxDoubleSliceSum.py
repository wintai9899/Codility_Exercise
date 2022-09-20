
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    A = [3,2,6,-1,4,5,-1,2]

    1. get postfix sum of A[1:]
    LeftToRight = [0,2,8,7,11,16,15,0]

    2. get postfix sum in reverse order
    RightToLeft = [0,16,14,8,9,5,0,0]

    3. tempArr = LeftToRight[i] + RightToLeft[i+2]

                [14,10,17,12,11,16,17]

                ans: 17
    """

    LeftToRight = [0] * len(A)
    RightToLeft = [0] * len(A)
    leftSum = 0

    for i in range(1, len(A ) -1):
        leftSum += A[i]
        if leftSum < 0:
            leftSum = 0

        LeftToRight[i] = leftSum

    rightSum = 0

    for i in range(len(A ) -2, 0, -1):
        rightSum += A[i]

        if rightSum < 0:
            rightSum = 0

        RightToLeft[i] = rightSum

    print(LeftToRight)
    print(RightToLeft)


    res = 0
    for i in range(len(A) - 2):
        totalSum = LeftToRight[i] + RightToLeft[ i +2]
        print(totalSum)
        res = max(res ,totalSum)

    return res


print(solution([3,2,6,-1,4,5,-1,2]))
