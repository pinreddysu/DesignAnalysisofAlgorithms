import math as mt
"""Merging properly!"""
def mergesort(A,inversionlist,inversions):
    if len(A) == 1:
        return A #get the array if only one element
    else:
        q = mt.floor(len(A)/2) #getting the floor value
        L = [0] * (q) #initializing all values with 0 on left side array
        R = [0] * (len(A) - q) #initializing all values with 0 on right side array
        if len(A)%2!=0:
            n = q+1
        else:
            n = q

        #copying array in left and right ones separated by 'q'    
        for i in range(q):
            L[i] = A[i]
        for j in range(n):
            R[j] = A[j+q]
        LS = mergesort(L,inversionlist,inversions) #applying recurive function for left side array
        RS = mergesort(R, inversionlist,inversions) #applying recurive function for right side array
        data, inversions = Merge(LS,RS,inversions) #Merging the data back into sorted manner
        inversionlist.append(inversions) #saving all inversions in a list step by step and calculating sum of all the values to get total inversions
        return data
def Merge(L,R,inversions):
    B = [0] * (len(L)+len(R)) #assigning 0 to all positions in new array for combining left and right arrays
    i = 0
    j = 0
    count = 0
    for k in range(len(B)):
        #if right values are greater than left ones, then simply copy into the new array and no inversions
        if j > len(R)-1 or (i<=len(L)-1 and L[i].val<=R[j].val):
            B[k] = L[i]
            count = 1
            i = i +1
            count = 0
        else: #if right values are smaller than left values, then copy them to the new array 
            B[k] = R[j]
            if count ==0:
                inversions+=(len(L))-i #calculating inversions by distance required to travel by value to reach its desired position(length of left array - current position)
            j = j+1

    return B,inversions