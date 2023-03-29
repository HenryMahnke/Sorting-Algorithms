# given some unsorted array such as

x = [64, 1, 12, 40, 11, 11,19]
# x = [1,1,4,1]

# we want to find some sorted array

y= [1,2,3,4]

# ascending order, or:

z= [4,3,2,1]

# decending order:

min_index_value = 0


for i in range(len(x)):
    # find the min element
    for j in range(len(x)):
        if x[j] > x[i]:
            old_value = x[i]
            new_value = x[j]
            # need to swap places somehow
            x[i] = new_value # swap cur index with min index
            x[j] = old_value

print(x)