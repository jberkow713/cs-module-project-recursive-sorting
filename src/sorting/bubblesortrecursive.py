def recursive_bubble_sort(arr, unsorted_length):
    # base case(s)
    # how do we get closer to a base case
    #length of unsorted portion = 0 could be base case
    # so we have to subtract 1 from length of unsorted portion
    # to get get closer to the base case
    # each pass on its own does same thing in the iterative case
    
    
    if unsorted_length > 0:
        #shorten array by 1 each time, the unsorted length -1 is
        #how you reach the base case of 0
        # it will sort the entire array -1,
        # so if you start at length of 9, it sorts 8,
        # in order to sort 8 it has to sort 7, 
        # and so on, until it reaches the base case of 0, 
        # where it will simply end the loop, and return the array
        recursive_bubble_sort(arr, unsorted_length-1)
    
    for i in range (unsorted_length -1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr            



arr = [13, 15, 6, 19, 27]
print(recursive_bubble_sort(arr, len(arr))) 