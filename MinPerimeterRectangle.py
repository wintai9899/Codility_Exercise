def solution(N):

    if not N:
        return 0
    # find sqrt of N as N = length * width
    # finding sqrt of N allows length approx = width 

    x = int(N ** 0.5)
    res = float("inf")
    while x > 0:
        y = N / x

        if y.is_integer():
            perimeter = 2 * int(x + y)
            res = min(res, perimeter)
        x -= 1

    return res