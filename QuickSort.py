def quickSort(arr, low, high):
    if low < high:
        part = separate(arr, low, high)
        quickSort(arr, low, part-1)
        quickSort(arr,part+1, high)

def separate(arr, low, high):
    j=0
    i =-1
    pivot = arr[high] # a value within the array
    i = low-1
    for j in range(low, high-1):
        if(arr[j] < pivot):
            i +=1 
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i+1] 
    arr[i+1] = arr[high]
    arr[high] = temp
    return(i +1)
arr = [6,1,4,7,2]
print(arr)
quickSort(arr,0,4)
print(arr)
#im insane, it actually works 
