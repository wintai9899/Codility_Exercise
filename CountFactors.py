def solution(N):
    """
    find the max number which holds the condition number ** 2 < N

    [1,2,3,4,|5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            limit = 4

    2. Find the factors in [1,2,3,4]

    3. result = Multiply the number of factors by 2

    4. If N has square root. return res - 1 , else return res
    """
    counter = 0
    squareRoot = int(N ** 0.5)

    for i in range(1, squareRoot + 1):
        if N % i == 0:
            counter += 1

            # if N has a square root
    if N == squareRoot * squareRoot:
        res = (counter * 2) - 1

    else:
        res = counter * 2

    return res