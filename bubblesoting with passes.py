from itertools import count


def bubblesortingwithpasses(arr, n):
    if n == 1:
        return
    it = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            it +=1
            print(arr)
            print(it)
    bubblesortingwithpasses(arr , n-1)

arr = [8, 3, 5, 2, 7, 6]
n = len(arr)
bubblesortingwithpasses(arr , n)
print(f"At last the list : {arr}")
