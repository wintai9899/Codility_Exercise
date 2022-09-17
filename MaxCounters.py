def solution(N, A):
    counters = [0] * N
    startLine = 0
    currentMax = 0

    for i in A:
        x = i - 1

        if i > N:
            startLine = currentMax

        # push elements to startline
        elif counters[x] < startLine:
            counters[x] = startLine + 1

        # increment by 1
        else:
            counters[x] += 1

        # found new maximum
        if i <= N and counters[x] > currentMax:
            currentMax = counters[x]

    for i in range(len(counters)):
        # push elements to startline
        if counters[i] < startLine:
            counters[i] = startLine

    return counters

