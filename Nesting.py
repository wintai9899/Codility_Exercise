def solution(S):
    count = 0

    for char in S:
        if char == "(":
            count += 1

        else:
            count -= 1

            if count < 0:
                return 0

    return 1 if not count else 0

