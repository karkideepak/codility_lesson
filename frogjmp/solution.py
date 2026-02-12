def solution(X, Y, D):
    # If already at or beyond target
    if X >= Y:
        return 0
    
    distance = Y - X
    
    # Compute minimal jumps using ceiling division
    return (distance + D - 1) // D
