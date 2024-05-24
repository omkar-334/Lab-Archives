class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = profit / weight


def knapsack(capacity: int, profits: list, weights: list):
    items = [Item(i, j) for i, j in zip(profits, weights)]
    items.sort(key=lambda x: x.ratio, reverse=True)
    value = 0
    for item in items:
        if item.weight <= capacity:
            capacity -= item.weight
            value += item.profit
        else:
            temp = item.profit * capacity / item.weight
            value += temp
            capacity = 0
    return value


capacity = int(input("Enter the capacity of the knapsack: "))
num_items = int(input("Enter the number of items: "))

print("Enter the profits and weights as space-separated arrays:")
profits = list(map(int, input("Profits: ").split()))
weights = list(map(int, input("Weights: ").split()))

value = knapsack(capacity, profits, weights)
print(f"The maximum value that can be obtained is: {value}")
