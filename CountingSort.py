def CountingSort(arr):
    print("arr", arr)     
    output = [0]*len(arr)
    temp = [0]*8
    mod_temp = temp
    for n in arr:
        temp[n] = temp[n] +1
    for n in range(len(temp)):
        if(n>0):
            mod_temp[n] = temp[n] +temp[n-1]
        else:
            mod_temp[n] = temp[n]
    print("temp", temp)
    print("mod_temp", mod_temp)
    for n in range(len(arr)):
        index = mod_temp[arr[n]]
        # arr[n] returns the value of the given array, some number 1-7
        # then, the mod_temp of that array value gives us the number of positions "before"
        # that value in the array, therefore, we can place that value arr[n]
        # at that index in the output array
        # aka at n =0, arr[0] = 1, mod_temp[1] = 2, aka, there are 2 places(inclusive) prior to the value of 1
        # but because that is in occurances, we need to decrement index to convert to actual places 2-1 is 1
        # because we do this, we can now say that there is 1 place prior to that 1, which will be a lower number, 
        # or in our case, another 1, we cna do this by decrementing that mod_temp value such that it will fill in later
        
        output[index-1] = arr[n]
        # we need to decremenent the index, because we are converting from
        # base 1 numbering as in # of occurances to indexes, which is base 0
        mod_temp[arr[n]] -= 1
        print("n", n, "index", index, "value", arr[n])
        print("mod_temp", mod_temp)
        print("output", output)
    print(output)
arr = [1,4,1,2,7,5,2]
CountingSort(arr)