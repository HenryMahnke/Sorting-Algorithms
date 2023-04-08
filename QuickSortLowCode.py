def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        # contains all elements less than the pivot using funny python stuff
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
arr = [6,1,4,7,2,3]
# arr = [6,1,4,7,2,9,3,2,34,123,16,17,1,32,2,15,1,71,123,36,22,116]
print(arr)
arr = quicksort(arr)
print(arr)