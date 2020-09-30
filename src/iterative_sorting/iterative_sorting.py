# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #Assign a variable to the len method on the array
    arrLen = len(arr)
    #Loop through your array
    for i in range(0, arrLen):
        #Assign a variable to false.  When no items have been swapped this variable will remain False.
        swapped = False
        #iterate through for the length of the array but adjust so that the iteration goes one less index each time (Or iterate for the remaining indexes after each iteration)
        #This adjust for the final two values in the iteration that will be solved.
        for j in range(0, arrLen-i-1):
        #Compare each element to its neighbor
            if arr and arr[j] > arr[j+1]:
                #Swap the elements if the item on the left is larger than right
                arr[j], arr[j+1] = arr[j+1], arr[j]
                #Update the swapped variable because a swap has happened
                swapped = True
        #If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
        if swapped == False:
            print(arr)
            return arr
    return arr           

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
