def counting_sort(A,digit,radix):
    # this initializes an array of length n
    Sorted = [0] * len(A)
    C = [0]*int(radix)

    for i in range(0,len(A)):
        digit_of_Ai = (A[i]/radix**digit)%radix