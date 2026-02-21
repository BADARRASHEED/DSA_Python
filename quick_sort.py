def quick_sort(arr):
    # Base case: if list has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (here we take middle element)
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively sort left and right parts
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2]
    sorted_arr = quick_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)