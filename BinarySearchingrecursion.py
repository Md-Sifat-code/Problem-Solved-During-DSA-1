def binarysearchingusingrecursion(arr, left, right, key):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binarysearchingusingrecursion(arr, left, mid - 1, key)
    else:
        return binarysearchingusingrecursion(arr, mid + 1, right, key)

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
key = 50
result = binarysearchingusingrecursion(arr, 0, len(arr) - 1, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
