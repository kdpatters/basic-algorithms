'''
Common sorting algorithms including merge sort, insertion sort, bubble sort,
quick sort, and counting sort.
'''

def merge_sort(big_list, head=0, tail=-1, ascending=True):
    '''
    Recursively sort a list with elements that can be compared from 
    smallest to largest.
    :big_list: a list or tuple with comparable elements
    :head: start index of list to sort in `big_list`
    :tail: last index of list to sort in `big_list`
    :ascending: boolean for whether to sort from smallest to largest
    '''

    # Ensure tail gives index counting from start of list
    if (tail == -1): tail += len(big_list)

    ## Base case: list contains 0 or 1 element
    length = tail - head + 1 # Add one to count the element at the head
    if (length <= 1):
        return big_list[head:tail + 1]

    ## Recursive case: split list and call function again
    # Compute approximate number of elements in half the list
    half = head + (length / 2)
    first_half = merge_sort(big_list, head=head, tail=(half - 1), 
        ascending=ascending)
    # May contain 1 more element than in first half
    second_half = merge_sort(big_list, head=half, tail=tail,
        ascending=ascending)
    
    ## Iterate through sorted lists and merge them
    curr_1st = 0 # Index of current element in first list
    curr_2nd = 0 # Index of current element in second list
    new_list = [first_half[0],] * length # Initialize empty list
    i = 0
    while (i < len(new_list)):
        # Check if we have run out of elements in first list
        if (len(first_half) == curr_1st):
            # Set the rest of the new list to the rest of the second list
            new_list[i:] = second_half[curr_2nd:]
            i = len(new_list) # Set stopping condition
        # Check if we have run out of elements in second list
        elif (len(second_half) == curr_2nd):
            # Set the rest of the new list to the rest of the first list
            new_list[i:] = first_half[curr_1st:]
            i = len(new_list) # Set stopping condition
        else:    
            # Check if current element in first list is bigger than current                 # element in the second list        
            first_bigger = first_half[curr_1st] >= second_half[curr_2nd]
            if (ascending == first_bigger):
                new_list[i] = second_half[curr_2nd]
                curr_2nd += 1
            else:
                new_list[i] = first_half[curr_1st]
                curr_1st += 1
            i += 1
    return new_list  
