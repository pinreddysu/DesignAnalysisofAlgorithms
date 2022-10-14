def insertionSort(array):
    inversions = 0
    #outer loop checking each element staring from second element 
    for incr in range(1, len(array)):
        key = array[incr]
        j = incr - 1  
    
        # Comparing key with each element on left until smaller value is found   
        while j >= 0 and key.val < array[j].val:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it
        array[j + 1] = key
        inversions+=incr-(j+1) #calculating inversions by checking how many numbers a value had to cross to reach its appropriate destination
    return inversions