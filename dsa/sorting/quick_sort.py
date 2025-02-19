def quicksort(arr: list[int], left: int = 0, right: int | None = None) -> None:
    if right is None:
        right = len(arr) - 1
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)
    return


def partition(arr: list[int], left: int, right: int) -> int:
    pivot_index = get_pivot_index(arr, left, right)
    pivot = arr[pivot_index]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[pivot_index] = arr[pivot_index], arr[i + 1]
    return i + 1


def get_pivot_index(arr: list[int], left: int, right: int) -> int:
    return right


if __name__ == "__main__":
    arr = [2, 4, 1, 7, 3, 9]
    quicksort(arr)
    print(arr)
