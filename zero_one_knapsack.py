"""0/1 Knapsack implementation using bottom-up dynamic programming."""

from typing import Sequence


def zero_one_knapsack(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Return the maximum value that fits in the knapsack.

    This solves the classic 0/1 knapsack problem where each item can be used
    at most once.

    Args:
        weights: Weight of each item.
        values: Value of each item (same index corresponds to same item).
        capacity: Maximum total weight allowed in the knapsack.

    Returns:
        The maximum achievable value without exceeding capacity.

    Raises:
        ValueError: If `weights` and `values` lengths differ or capacity is negative.

    Time Complexity:
        O(n * capacity), where n is number of items.

    Space Complexity:
        O(n * capacity) for the DP table.
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length.")
    if capacity < 0:
        raise ValueError("capacity cannot be negative.")

    n = len(weights)

    # dp[i][w] stores the best value using first i items with capacity w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table row by row (item by item).
    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]

        for w in range(capacity + 1):
            if item_weight <= w:
                # Option 1: skip current item.
                exclude_item = dp[i - 1][w]

                # Option 2: include current item once, then use best of remaining capacity.
                include_item = dp[i - 1][w - item_weight] + item_value
                dp[i][w] = max(exclude_item, include_item)
            else:
                # Current item does not fit, so carry forward previous best.
                dp[i][w] = dp[i - 1][w]

    # Answer is the best value using all items at full capacity.
    return dp[n][capacity]


if __name__ == "__main__":
    # Example usage
    sample_weights = [2, 3, 4]
    sample_values = [3, 4, 5]
    sample_capacity = 5

    best_value = zero_one_knapsack(sample_weights, sample_values, sample_capacity)
    print("Maximum value in Knapsack =", best_value)
