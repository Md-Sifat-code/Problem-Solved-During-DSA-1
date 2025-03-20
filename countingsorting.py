#logic
#Firstly lets take the max element from the input array
# Then we need to take a new list based on the max element +1
#Then we need to incriment every index of the count_arr based on the element of the arr
# Then count_arr er protita element er jnno prefix sum beer kora lagbe
# Then akta new list nibo for the the ourput list
# Then main arr er reverse side theke protita num er jonnocount arr theke 1 minus kore dibo .
# Then count arr er modde oi num er idex e jei value ta ase seitake output er index number dhore num take bosabo



def countingsorting(arr):
    M = max(arr)
    count_arr = [0] * (M+1)
    for num in arr:
        count_arr[num] +=1
    for i in range(1, M+1):
        count_arr[i] += count_arr[i-1]
    output = [0]*len(arr)
    for num in reversed(arr):
        count_arr[num] -=1
        output[count_arr[num]] = num
    return  output


arr = [5,2,1,4,4,6,1]
result = countingsorting(arr)
print(result)