def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        # this only works because L is then "set" to the new value, and mutated, and that is reflected in the paused recursive loops
        # because python is neither pass by value or pass by reference, this is uses assignment reference, and is called using object attributes
        #that allows me to implicitly set the values of L and R, such that they can be sorted at a lower level of the recursive tree
        #but can then be referenced in higher levels of the tree when they are being remerged
        mergeSort(R)


        #with the elements now at their lowest respective levels
        #often referred to as atomic level, we can begin to sort through them 
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] <R[j]:
                arr[k] = L[i]
                #this is that object attribute I was referincing, that will "set" the value of the upper function's value
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k+=1
        #what this function does is it will sort through both lists, whether atomic or not, and begin to set the upper level array to the correct values in their correct order
        # the problem with this enlies if you have lets say [1,3,7] and [2,4,5]
        #when you get to the end of one list, you need to add the remaining items to the end of the array
        while i<len(L):
            arr[k] = L[i]
            k +=1
            i+=1
        while j<len(R):
            arr[k] = R[j]
            k+=1
            j+=1

arr = [6,1,4,7,2,9,3,2,34,123,16,17,1,32,2,15,1,71,123,36,22,116]
print(arr)
mergeSort(arr)
print(arr)
#im insane, it actually works 
