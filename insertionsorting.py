def insertionsecore(arr, n):
    i =1
    while i<n:
        if i > 0 and arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1], arr[i]
            i-=1
        else:
            i+=1

arr =[3,2,1,5,12,7,2,1,54,3,21,5,6,7,8,3]
n = len(arr)
insertionsecore(arr,n)
print(arr)