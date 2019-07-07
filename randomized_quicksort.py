"""Author - Anantvir Singh, concept reference:= CLRS"""

"""Randomized selection of pivot results in expected running time E(T(n)) = O(nlogn) because the resulting recursion tree
has O(logn) levels and work done on each level is O(n), for mathematical analysis refer to CLRS page 179"""

import random
def randomized_partition(A,p,r):
    i = random.randint(p,r) # Randomized selection of pivot
    temp = A[r]             # exhcange A[r] with A[i]
    A[r] = A[i]
    A[i] = temp
    return partition(A,p,r)

def partition(A,p,r):
    x = A[r]                # pivot is last element (Its non randomized quicksort)
    i = p-1                 # initialize i to index -1
    for j in range(p,r):    # loop from j=0 to r-1
        if A[j] <= x:       # if jth element is less than pivot
            i += 1          # increment i
            temp = A[j]     
            A[j] = A[i]     # Swap A[i] and A[j]
            A[i] = temp
    temp = A[i+1]           # after for loop ends, swap i+1 th element with the pivot(the last element)
    A[i+1] = A[r]
    A[r] = temp
    return i+1              # return index of q. All elements to left of q i.e A[0] to A[q-1] are less than A[q]

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)  # 1st recursive call on left subarray excluding the element A[q]
        quicksort(A,q+1,r)  # 2nd recursive call on right subarray excluding the element A[q]

arr = [85,24,63,45,17,31,96,50]
quicksort(arr,0,len(arr)-1)
print('Result is :-',arr)
