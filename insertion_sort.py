def insertion_sort(list):
    #For every number in the list... which begins at the second number in the list
    for i in range(1, len(list)):
        #assign the current number being looked at to a variable
        current = list[i]
        #assign the current number to a variable for running a while loop.  
        j = i
        #check that the value is greater than zero and that the current number is less than the one to its left
        while j > 0 and current < list[j-1]:
            #Assign the value to the left to the current position (move to the right)
            list[j] = list[j-1]
            #Change the id to be one less to move the number to the left
            j -= 1
            #Sets the value at the current index to the current number
            list[j] = current
    return list

print(insertion_sort([8,3,4,1,5,6,22,99]))