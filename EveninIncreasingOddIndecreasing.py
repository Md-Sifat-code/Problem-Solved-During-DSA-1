def evensorting(arr, n):
    i = 1
    while i < n:
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
        else:
            i+=1
    return  arr

def oddsorting(arr , n):
    i = 0
    while i < n:
        if i > 0  and arr[i] > arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            i += 1
    return arr

def eveninincreasingoddindecreasing(arr,n):
    evenpart = []
    oddpart = []
    for element in arr:
        if element%2 == 0:
            evenpart.append(element)
        else:
            oddpart.append(element)
    sortedeven = evensorting(evenpart, len(evenpart))
    sortedodd = oddsorting(oddpart, len(oddpart))
    arr.clear()
    arr.extend(sortedeven)
    arr.extend(sortedodd)


numbers = [0, 1, 2, 3, 4, 5, 6, 7]
eveninincreasingoddindecreasing(numbers, len(numbers))
print(numbers)