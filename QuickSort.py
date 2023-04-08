def quickSort(arr, low, high):
    if low < high:
        part = separate(arr, low, high)
        quickSort(arr, low, part-1)
        quickSort(arr,part+1, high)

def separate(arr, low, high):
    j=low # 0
    pivot = arr[high] # 7
    i = low-1 #-1
    print(pivot)
    for j in range(low, high): 
        if(arr[j] < pivot): 
            i +=1 
            print(arr)
            print("i",i,"arrValue I", arr[i])
            print("j",j,"arrValue J", arr[j])
            if j != i:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            print(arr)
            # this puts all of the values that are less than the pivot on the left side of the array
    temp = arr[i+1] 
    arr[i+1] = arr[high]
    arr[high] = temp
    # because the ith element is the last element less than the pivot, the i+1 index must be the pivot, therefore we can place it in it's cporrect spot
    return(i +1)
arr = [6,1,4,7,2,3]
# arr = [6,1,4,7,2,9,3,2,34,123,16,17,1,32,2,15,1,71,123,36,22,116]
print(arr)
quickSort(arr,0, 5)
print(arr)
#im insane, it actually works 
