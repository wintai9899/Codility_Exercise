def solution(N, M):
    """
    number of chocolates = LCM(N,M) / M

    find LCM using formula LCM = a*b/GCD(a,b)
    :param N:
    :param M:
    :return:
    """
    LCD = int(N * M / findGCD(N, M))

    res = int(LCD / M)

    return res


def findGCD(N, M):
    while M:
        N, M = M, N % M

    return N