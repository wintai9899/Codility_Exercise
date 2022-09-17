def solution(A, B):
    # for downstream fishes
    stack = []
    eaten_count = 0

    for i in range(len(A)):
        # when encounter downstream fish
        if B[i] == 1:
            # append the size of the downstream fish
            stack.append(A[i])
        # when encounter upstream fish
        else:
            while stack:
                weight_down = stack[-1]
                # downstream > upstream
                if weight_down > A[i]:
                    eaten_count += 1
                    break

                else:
                    # upstream > downstream
                    stack.pop()
                    eaten_count += 1

    survivors = len(A) - eaten_count

    return survivors