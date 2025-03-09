
def selectionsorting(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index =j
        arr[i],arr[min_index] = arr[min_index],arr[i]


arr =[3,2,1,5,12,7,2,1,54,3,21,5,6,7,8,3]
n = len(arr)
selectionsorting(arr,n)
print(arr)