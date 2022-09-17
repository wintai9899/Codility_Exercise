def solution(A):
    candidate = 0
    count = 0
    candidate_count = 0
    # Finds the dominant (candidate) of A
    for i in range(len(A)):
        # label new species as candidate if count == 0
        if count == 0:
            candidate = A[i]
            count += 1

        elif A[i] != candidate:
            count -= 1

        else:
            count += 1

    # Get the count of candidates
    for animal in A:
        if animal == candidate:
            candidate_count += 1
    # if valid candidate: return the index
    if candidate_count > (len(A) // 2):
        return A.index(candidate)

    return -1