# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    merged_arr = []
    
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_arr.append(left[left_index])
            left_index +=1 
        else:
            merged_arr.append(right[right_index])
            right_index +=1
    merged_arr += left[left_index: ]
    merged_arr += right[right_index: ]
    return merged_arr     

print(merge([1,3,5],[4,7,9]))           

#compares 1st item in left and right array: if left is smaller, appends left
# if right is smaller appends right
# whichever is smaller, move one index over and compare the 1st element to 0 element
# and continue down the list until you finish emptying one full list,
# and then at this point, you append the rest of the items in the left list
# and then append the rest of the items in the right list,
# then the merged array is complete with all values from left and right,
# and then you return the merged_array
def merge_sort(arr):

    if len(arr) <=1:
        return arr
    
    # makes all elements into 1 sized arrays,
    # uses previous merge function to put all elements back together
    midpoint = int(len(arr)/2)     # to cater for a being odd
    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)    

# TO-DO: implement the Merge Sort function below recursively
'''
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
    # so if length of array is greater than 1, divide it in half,
    # left is everything up to the midpoint, right is everything past midpoint
    # then recursively call this function on itself, until basically everything 
    # is arrays of 1

        merge_sort(left)
        merge_sort(right)
    # so you have divided the array into many arrays of length 1


        i = 0
        j = 0
        k = 0
    
        while i < len(left) and j < len[R]:
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        # THE Above step is taking individual arrays of 1, comparing them to 
        # each other, inserting them back into lists of 2,
        # comparing those lists of 2 to each other, and so on and so forth,
        # until you have 2 halves, then comparing those values and recreating the 
        # original list
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr                     


        # so this should divide the arrays continuously until all arrays 
        # have length of 1
'''


   

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

