ages = [24, 18, 30, 22, 28]
def insertionsortingforages( arr , n):
    i = 1
    while i < n:
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
            print(arr)
        else:
            i+=1

n = len(ages)
insertionsortingforages(ages, n)
print(ages)