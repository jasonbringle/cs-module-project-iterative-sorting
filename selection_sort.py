def selection_sort(arr):
    #Loops thorugh array -1 because the last number will have nothing to compare to
    for i in range(0, len(arr) - 1):
        #Assign a var to the current index
        cur_index = i
        #Assign and initial value of the current index to a var "smallest_index".  This will be our storage for the smallest number as it moves through iteration.
        smallest_index = cur_index
        #Start loop that compares the current number with the one next to it. (curr_index + 1)
        for j in range(cur_index + 1, len(arr)):
            #Check if the current smallest value is greater than the current location in the loop
            if arr[smallest_index] > arr[j]:
                #If true assign the smallest index to the current index.
                smallest_index = j
        #After the loop on the comparing number (j)... swap the value of the current_index with value of the smallest index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr
"""This sorting method uses a nested for loop to first compare if the first number in the 
outside loop is greater than the number to the right. If it is then it assigns inner loops number 
to a variable and continues iterating until it again finds a set where the number in the 
array is smaller than the smallest_index var. 

After it compares the first number in the array to all other numbers it does a swap to
make the current_index in the outer loop == the smallest_index var    and also swaps the smallest_index
var to be the current_index var  (This simple swaps what is identified as the smallest number found with the current
outside loops number)
"""

