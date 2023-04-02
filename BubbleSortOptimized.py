# this sorting method works by taking some array:
# [6,1,4,7,2,9]
# you compare the first 2 values, and preform a swap if needed 

arr = [6,1,4,7,2,9,3,2,34,123,16,17,1,32,2,15,1,71,123,36,22,116]

# Now we wanna think about how we can stop the algorithm from running if the sequence is already correct
# but how can you verify that it's correct without

def compare(arr):
    for j in range(len(arr)):
        swapped = False
        for i in range(len(arr)-j-1):
            first = arr[i]
            second = arr[i+1]
            if first>second:
                arr[i] = second
                arr[i+1] = first
                swapped = True
        if not swapped:
                # what this will do, is if there are NO swapping events it will break it
            return
        print(arr)
    print(arr)



compare(arr)