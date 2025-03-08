def bouble_sort (arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bouble_sort(arr, n-1)

arr = ["kola", "mango", "Apple", "Rice"]
bouble_sort(arr,len(arr))
print(arr)