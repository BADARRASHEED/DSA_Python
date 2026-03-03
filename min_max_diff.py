def max_min_difference(arr):
    """
    Computes the maximum and minimum possible total difference 
    when pairing elements of an even-length array.

    Strategy:
    ---------
    1. Maximum Difference:
       - Sort the array.
       - Pair smallest with largest.
       - Continue inward.

    2. Minimum Difference:
       - Sort the array.
       - Pair adjacent elements.

    Parameters:
    -----------
    arr : list of int/float
        Input list of numeric values.
        Length must be even.

    Returns:
    --------
    tuple (max_difference, min_difference)

    Raises:
    -------
    ValueError:
        If the length of the array is odd.
    """

    # Ensure array length is even
    if len(arr) % 2 != 0:
        raise ValueError("Array length must be even to form pairs.")

    # Work on a sorted copy (do not modify original list)
    sorted_arr = sorted(arr)

    n = len(sorted_arr)
    max_difference = 0
    min_difference = 0

    # ----------------------------
    # Maximum Total Difference
    # Pair smallest with largest
    # ----------------------------
    for i in range(n // 2):
        max_difference += abs(sorted_arr[i] - sorted_arr[n - 1 - i])

    # ----------------------------
    # Minimum Total Difference
    # Pair adjacent elements
    # ----------------------------
    for i in range(0, n, 2):
        min_difference += abs(sorted_arr[i] - sorted_arr[i + 1])

    return max_difference, min_difference


# ---------------------------------
# Example Usage
# ---------------------------------
if __name__ == "__main__":

    example_array = [5, 1, 9, 3, 8, 2]

    max_diff, min_diff = max_min_difference(example_array)

    print("Original Array :", example_array)
    print("Sorted Array   :", sorted(example_array))
    print("Maximum Total Difference :", max_diff)
    print("Minimum Total Difference :", min_diff)