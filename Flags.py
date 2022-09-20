# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    """
    A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

    peaks = [1, 1, 3, 3, 5, 5, 10, 10, 10, 10, 10, 12]
    """
    peaks = [0] * len(A)
    nextPeak = len(A)
    peaks[len(A) - 1] = nextPeak

    for i in range(len(A) - 2, 0, -1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            nextPeak = i

        peaks[i] = nextPeak
    peaks[0] = nextPeak

    current_guess = 0
    next_guess = 0

    while can_place_flags(peaks, next_guess):
        current_guess = next_guess
        next_guess += 1
        # next guess failed, so return current guess
    return current_guess


def can_place_flags(peaks, flags_to_place):
    current_position = 1 - flags_to_place
    for i in range(flags_to_place):
        # out of bounds
        if current_position + flags_to_place > len(peaks) - 1:
            return False

        current_position = peaks[current_position + flags_to_place]

    return current_position < len(peaks)