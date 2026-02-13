def selection_sort_asc(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Find the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort_desc(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current index is the maximum
        max_index = i

        # Find the largest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the maximum element with the first element
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)

    sorted_arr_asc = selection_sort_asc(arr.copy())
    print("Sorted array in ascending order:", sorted_arr_asc)

    sorted_arr_desc = selection_sort_desc(arr.copy())
    print("Sorted array in descending order:", sorted_arr_desc)