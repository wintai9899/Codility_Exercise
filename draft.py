
def solution(n):
    binary = dec_to_bin(n)

    maxZero = 0
    count = 0
    for char in binary:
        if char == "0":
            count += 1

        else:
            maxZero = max(maxZero, count)
            count = 0
    return maxZero

def dec_to_bin(n):
    res = []

    while n > 0:
        remainder = n % 2
        res.append(str(remainder))
        n = n // 2

    res.reverse()

    return "".join(res)

if __name__ == "__main__":
    #111001
    print(solution(1041))