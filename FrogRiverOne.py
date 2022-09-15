def solution(X, A):
    # <----River--->
    # [F,F,F,F,F,F]
    # position of leaves on river
    river_pos = [False] * (X + 1)
    counter = X

    for i in range(len(A)):
        # position of leaf at time i
        pos = A[i]

        # position has no leaf
        if not river_pos[pos]:
            # mark true
            river_pos[pos] = True
            counter -= 1

            if counter == 0:
                return i

    return -1