def bubble_sort(arr):
    arrLen = len(arr)
    for i in range(0, arrLen):
        swapped = False
        for j in range(0, arrLen-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr + addedList
    return addedList

addedList = [9,8,7,6,5,4,3,2,1]
list = [8,7,6,5,4,3,2122112,44,5,6,3,2,67,8989,7,43,3]
print(bubble_sort(list))

#Bubble sort looks at the pairs of numbers in an array iterativly and determines whether the value on the left is greater 
#than the right. It then moves the numbers accordingly (low on left hight on right)
#Because you have to sort the entire list you not only want to iterate over the entire list once but how ever many times
#is equal to the length MINUS the index number MINUS one.  This looks at all the numbers except the previous iterations last
#number in the array. That number has already been sorted.
#The above solution includes a key that says whether the list has gone through a swap.  It updates on the action of swapping
#the numbers... it's base state is formed on the outside loop as False.  When the inner loop has finished and there are no
#more iterations to run through it will run throught to the if statement and check if the swapp variable is False...if so
#it will return out of the block of code.