def solution(A, B):
    count = 0
    for i in range(len(A)):

        a = A[i]
        b = B[i]

        GCD = gcd(a, b)
        while (gcd(a, GCD) != 1):
            a /= gcd(a, GCD)

        while (gcd(b, GCD) != 1):
            b /= gcd(b, GCD)

        if a == 1 and b == 1:
            count += 1

    return count


def gcd(A, B):
    while B:
        A, B = B, A % B

    return A 