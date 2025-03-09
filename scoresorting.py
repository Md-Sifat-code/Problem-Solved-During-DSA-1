def bubblesorting(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]

    bubblesorting(arr,n-1)

arr =[3,2,1,5,12,7,2,1,54,3,21,5,6,7,8,3]
n = len(arr)
bubblesorting(arr,n)
print(arr)
