def solution(X, Y, D):
    # If the frog is already at or beyond the target position,
    # no jumps are needed.
    if X >= Y:
        return 0

    # Calculate the total distance the frog still needs to cover.
    distance = Y - X

    # We need the smallest number of jumps such that:
    # X + jumps * D >= Y
    #
    # This is equivalent to:
    # jumps >= (Y - X) / D
    #
    # To avoid floating-point arithmetic, we use integer
    # ceiling division formula:
    # ceil(distance / D) = (distance + D - 1) // D
    jumps = (distance + D - 1) // D

    # Return the minimal number of jumps required.
    return jumps
