def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio for each item
    ratio = [v / w for v, w in zip(values, weights)]

    # Sort items by ratio in descending order
    items = sorted(zip(weights, values, ratio), key=lambda x: x[2], reverse=True)

    total_value = 0.0
    for weight, value, _ in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take the fraction of the remaining capacity
            total_value += value * (capacity / weight)
            break  # Knapsack is full

    return total_value


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = fractional_knapsack(weights, values, capacity)
print(f"Maximum value in Knapsack = {max_value}")
