def bubble_sort(arr: list[int], start: int = 0, end: int | None = None) -> list[int]:
    print(arr[start:end])
    if end is None:
        end = len(arr)
    if start == end:
        return
    for i in range(start, end - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort(arr, start=start, end=i)
    return
    
    
if __name__ == "__main__":
    arr = [2, 4, 1, 7, 3, 9]
    bubble_sort(arr)
    print(arr)