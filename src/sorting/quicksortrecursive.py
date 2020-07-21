#partition function handles work selecting pivot element
# and partitioning the data in array around the pivot element
#returns left partition, the pivot, and the right partition

def partition(arr):
    # pick the first element as the pivot element
    pivot = arr[0]
    left = []
    right = []

    #iterate through rest of array, putting each element in
    # appropriate bucket

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right             


def quicksortrecursive(arr):

    # base case
    if len(arr) <= 1:
        return arr
    # how do we get closer to base case?
    left, pivot, right = partition(arr)
    # basically, then function is taking an array, cutting off the end item, 
    # sorting the other items in 2 lists
    # becausse the pivot now is 1 item, the quicksort function 
    # will simply return it as a single element called pivot,
    # it then runs again on the new left and right lists
    # which divides them into a pivot, and more short lists, until it has returned
    # all elements in sequential order in 1 len arrays, and then it simply 
    # concats them all together, and returns the new array

    return quicksortrecursive(left) + [pivot] + quicksortrecursive(right)
