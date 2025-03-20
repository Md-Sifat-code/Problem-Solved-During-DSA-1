#logic
#Firstly lets take the max element from the input array
# Then we need to take a new list based on the max element +1
#Then we need to incriment every index of the count_arr based on the element of the arr
# Then count_arr er protita element er jnno prefix sum beer kora lagbe
def countingsorting(arr):
    M = max(arr)
    count_arr = [0] * (M+1)
    for num in arr:
        count_arr[num] +=1
    for i in range(1, M+1):
        count_arr[i] += count_arr[i-1]