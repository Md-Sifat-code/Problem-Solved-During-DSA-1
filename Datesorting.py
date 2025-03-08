def datesorting(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        # Correct the syntax error in the condition
        if arr[i][2] > arr[i+1][2] or (arr[i][2] == arr[i+1][2] and arr[i][1] > arr[i+1][1]) or (arr[i][2] == arr[i+1][2] and arr[i][1] == arr[i+1][1] and arr[i][0] > arr[i+1][0]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    datesorting(arr, n-1)

arr = [[23, 12, 2003], [3, 2, 2001], [1, 2, 2008]]
n = len(arr)
datesorting(arr, n)
print(f"Sorted dates: {arr}")

# So the logic is here first compare between the years . then when the years will be eaqual then check the months , then when you found the months are equal then check is the data are bigger
# then swap it