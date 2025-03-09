arr = [10,5,6,3,2,20,100,80]
n = len(arr)

def wavebubble(arr,n):
    for i in range(n - 1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1] , arr[i]

        i+=2


wavebubble(arr , n)
print(arr)
