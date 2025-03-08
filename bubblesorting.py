def bubble_sorting(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i]> arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
    bubble_sorting(arr,n-1)

arr = [5,1,3,2,7,8]
n = len(arr)
bubble_sorting(arr, n)
print(arr)