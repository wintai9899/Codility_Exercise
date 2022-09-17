class DiscLog():
    # x : x - coordinate
    # start_end: indicates whether its a start or end
    # 1 : start point, -1 : end point
    def __init__(self, x, start_end):
        self.x = x
        self.start_end = start_end

"""
Sort it like intervals
"""
def solution(A):
    discHistory = []
    active_intersections = 0
    count = 0
    for i in range(len(A)):
        discHistory.append(DiscLog(i - A[i], 1))
        discHistory.append(DiscLog(i + A[i], -1))

    # sort discHistory
    discHistory.sort(key=lambda i: (i.x, -i.start_end))

    for log in discHistory:
        active_intersections += log.start_end

        if log.start_end > 0:
            count += active_intersections - 1

    return count if count <= 10000000 else -1

