def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def divide(arr, l, r):
    if l < r:
        m = (l + r) // 2
        divide(arr, l, m)
        divide(arr, m + 1, r)
        merge(arr, l, m, r)


def merge_sort(arr):
    divide(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    merge_sort(arr)
    print("\n\tAfter applying merge sort\n")
    print("Sorted array:", arr)
