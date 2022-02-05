# Bubble Sort
def bubble_sort(the_list):
    print(f"Original List:\t{the_list}")
    n = len(the_list)

    # Pass through the list n - 1 times
    for i in range(1, n):

        # Go from the first item to the last unsorted item. 
        for j in range(1, n - i + 1):
            if the_list[j] < the_list[j-1]:
                temp = the_list[j-1]
                the_list[j-1] = the_list[j]
                the_list[j] = temp

        print(f"Pass {i}:\t\t{the_list}")
    return the_list


# Optimized Bubble Sort
def optimized_bubble_sort(the_list):
    print(f"Original List:\t{the_list}")
    n = len(the_list)

    # Pass through the list n - 1 times
    for i in range(1, n):
        swapped = False
        # Go from the first item to the last unsorted item. 
        for j in range(1, n - i + 1):
            if the_list[j] < the_list[j-1]:
                temp = the_list[j-1]
                the_list[j-1] = the_list[j]
                the_list[j] = temp
                swapped = True

        print(f"Pass {i}:\t\t{the_list}")

        if swapped == False:
            break

    return the_list

# Selection Sort
def selection_sort(the_list):
    n = len(the_list)
    print(f"Original List:\t{the_list}")
    for i in range(n-1):
        min_index = i # index of the smallest item
        for j in range(i+1, n):  # sequential search for smallest item
            if the_list[j] < the_list[min_index]:
                min_index = j
                
        temp = the_list[i]
        the_list[i] = the_list[min_index]
        the_list[min_index] = temp

        print(f"Pass {i+1}:\t\t{the_list}")

# Insertion Sort
def insertion_sort(the_list):
    print(f"Original List:\t{the_list}")
    n = len(the_list)
    i = 1
    while i < n:
        if the_list[i-1] > the_list[i]:
            temp = the_list[i]  # don't erase current item from memory
            j = i - 1
            # shift each item to the right that needs to be shifted
            while j >= 0 and the_list[j] > temp:    # repeat?
                the_list[j+1] = the_list[j] #shift
                j -= 1                  # move down
                the_list[j+1] = temp    # place temp
            
        print(f"Pass {i}:\t\t{the_list}")
        i += 1