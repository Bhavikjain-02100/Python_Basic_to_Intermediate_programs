def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Given values, weights, and capacity
values = [40, 50, 60]
weights = [20, 30, 40]
capacity = 60

# Calculate the maximum value that can be achieved
max_value = knapsack(values, weights, capacity)
print("Maximum value that can be achieved:", max_value)
