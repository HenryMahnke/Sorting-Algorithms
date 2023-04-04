def CountingSort(arr):
    output = [0]*len(arr)
    temp = [0]*8
    mod_temp = temp
    print(temp)  
    for n in arr:
        print(n)
        temp[n] = temp[n] +1
    print(temp)        
    for n in range(len(temp)):
        mod_temp[n] = temp[n] + temp[n-1]
    print(mod_temp)
    mod_temp
    for n in range(len(mod_temp)):
        mod_temp[n] -= 1
    print("mod_temp", mod_temp)
    print("arr", arr)

arr = [1,4,1,2,7,5,2]
CountingSort(arr)