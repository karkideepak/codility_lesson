def solution(N):
    max_gap = 0
    current_gap = 0
    started = False  # becomes True after the first '1'

    while N > 0:
        if N & 1:  # bit is 1
            if started:
                max_gap = max(max_gap, current_gap)
            else:
                started = True
            current_gap = 0
        else:  # bit is 0
            if started:
                current_gap += 1

        N >>= 1  # shift right

    return max_gap
