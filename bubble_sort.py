def bubble_sort(arr):
    """
    Sort a list in ascending order using the Bubble Sort algorithm (in-place).

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. With each pass, the largest
    unsorted element "bubbles" to its correct position at the end of the list.

    This implementation:
    - Sorts the list in-place (modifies the original list)
    - Uses an optimization to stop early if the list is already sorted

    Parameters
    ----------
    arr : list
        A mutable list of comparable elements (e.g., int, float, str).

    Returns
    -------
    None
        The input list is sorted in-place.

    Time Complexity
    ---------------
    Best Case:    O(n)    (already sorted, due to early termination)
    Average Case: O(n^2)
    Worst Case:   O(n^2)

    Space Complexity
    ----------------
    O(1) auxiliary space

    Properties
    ----------
    - In-place algorithm
    - Stable sorting algorithm
    - Comparison-based
    """

    n = len(arr)

    # Perform passes over the list
    for i in range(n):
        swapped = False  # Tracks whether any swap occurs in this pass

        # Last i elements are already in correct position
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]

    print("Before sorting:", data)

    bubble_sort(data)  # in-place modification

    print("After sorting: ", data)
