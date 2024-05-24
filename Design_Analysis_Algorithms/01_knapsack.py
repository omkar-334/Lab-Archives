def knapsack(weights, values, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items


capacity = int(input("Enter the capacity of the knapsack: "))
num_items = int(input("Enter the number of items: "))

print("Enter the profits and weights as space-separated arrays:")
profits = list(map(int, input("Profits: ").split()))
weights = list(map(int, input("Weights: ").split()))

max_value, selected_items = knapsack(weights, profits, capacity, num_items)
print("Max val:", max_value)
print("Selected items:", selected_items)
