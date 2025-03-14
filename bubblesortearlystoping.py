def bubblesortingearllystop( arr , n):
    if n == 1:
        return arr

    swaped = False
    for i in range(n):
        if arr[i]> arr[i+1]:
            arr[i], arr[i +1] = arr[i + 1], arr[i]

        swaped = True
    if not swaped:
        return arr

    bubblesortingearllystop(arr, n-1)

arr = [5,1,3,2,7,8]
n = len(arr)
bubblesortingearllystop(arr, n)
print(arr)