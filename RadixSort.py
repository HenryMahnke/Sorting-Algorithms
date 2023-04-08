def RadixSort(arr):
    max_value = max(arr) 
    exp = 1

    while exp<= max_value:
        buckets = [[] for _ in range(10)]
        # this makes this:
        # [[], [], [], [], [], [], [], [], [], []]
        # an array for each possible digit
        print(buckets)
        for n in arr:
            cur_digit = (n//exp) % 10 #extracts the current digit
            buckets[cur_digit].append(n)
            print(buckets)
            # this will result in something like this
            # [[170, 90], [], [802, 2], [], [24], [45, 75], [66], [], [], []]        
        arr=[]
        for bucket in buckets:
            arr.extend(bucket)
            # concatenates the arrays back together
        # [170, 90, 802, 2, 24, 45, 75, 66] results in this

        # now because they are already sorted by the least significant bit
        # when it loops over, any single digits, will be sorted sequentially
        # so if you have 2, 3 in the arr
        # those will fall into place on the next pass
        exp *= 10
    return arr
arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr = RadixSort(arr)
print(arr)