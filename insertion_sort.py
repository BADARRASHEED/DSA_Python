"""
Insertion Sort is a simple sorting algorithm that sorts an array
step by step. In each iteration, the current element is inserted
into its correct position within the sorted portion of the array.

Algorithm Steps:
1. Start from the second element.
2. Store the current element in a temporary variable (key).
3. Shift larger elements on the left side to the right.
4. Insert the key at its correct position.
"""


def insertion_sort(arr):
    """
    arr : iterable sequence (e.g., list)
        The sequence to be sorted.

    Returns:
        Sorted sequence (ascending order).
    """

    # Loop from the second element to the end of the array
    for i in range(1, len(arr)):

        key = arr[i]  # Current element to be positioned
        j = i - 1  # Index of the previous element

        # Shift elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at the correct location
        arr[j + 1] = key

    return arr


# Example run
if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    print("Before sorting:", data)

    insertion_sort(data)

    print("After sorting:", data)
