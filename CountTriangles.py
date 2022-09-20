def solution(A):
    res = 0 
    A.sort()
    #  c   b a
    # [2,2,3,4]
    for a in range(len(A)-1,-1,-1):
        b = a - 1
        c = 0 

        while c < b:
            # we have a valid triangle
            if A[c] + A[b] > A[a]:
                res += b - c
                b -= 1

            else:
                c += 1

    return res