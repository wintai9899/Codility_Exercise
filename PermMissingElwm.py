
def solution1(A):

    # N = expected Sum without missing number
    N = len(A) + 1

    #expectedSum = (N * (N + 1)) // 2

    for i in range(1, N):
        N += i

    return N - sum(A)

"""
Optimize using math formula to calculate expected sum
"""
def solution2(A):
    expectedSum = l