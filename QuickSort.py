inversions = 0
def QuickSort(A):
    if len(A) < 2:
        return A #return array if onlny one element

    #creating 3 subproblems: lessthan, equalto, greaterthan    
    less = []
    equal = []
    greater = []
    pivot = 0 #choosing pivot to be first value
    global inversions
    for i in range(len(A)):
        if A[i].val < A[pivot].val:
            less.append(A[i])
            #if value needs to go on less than array than has to cross greater than and equal to arrays, thus add their array lengths to calculate distance travelled to calculate inversions
            inversions = len(equal) + len(greater) + inversions
        elif A[i].val > A[pivot].val:
            greater.append(A[i])
            #No inversions if value simply add on the greeater than side
        elif A[i].val == A[pivot].val:
            equal.append(A[i])
            #if value needs to go on equalto side than has to cross greater than array, thus add the array length to calculate distance travelled to calculate inversions
            inversions = len(greater) + inversions
    return QuickSort(less) + equal + QuickSort(greater) #recursive call for the less than, equal, and greater than side
