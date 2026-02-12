def minCostRec(n, height):
    # If there is only one 
    # stair(0-based index)
    if n == 0:
        return 0

    # If there are only 2 stairs(0-based 
    # index), then frog can only take 
    # jump of size one
    if n == 1:
        return abs(height[n] - height[n - 1])

    return min(
        minCostRec(n - 1, height) + abs(height[n] - height[n - 1]),
        minCostRec(n - 2, height) + abs(height[n] - height[n - 2])
    )

def minCost(height):
    n = len(height)
    return minCostRec(n - 1, height)

height = [20, 30, 40, 20]
print(minCost(height))
