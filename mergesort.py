"""Author - Anantvir Singh, concept reference:= CLRS page 31"""

import math
def merge(A,p,q,r):
    n_1 = q - p + 1                     # calculate number of elements in each subarray from indices passed to the function call
    n_2 = r - q                         # calculate number of elements in each subarray from indices passed to the function call
    L = list()                          # create 2 arrays to hold the elements of halved array
    R= list()
    for i in range(n_1):                    
        L.insert(i,A[p+i])                # Put elements from given array 'A' into newly created L and R arrays 
        print(L[i]) 
    for j in range(n_2):
        R.insert(j,A[q+j+1])
    L.append(10000000000)                      # Sentinel 1
    R.append(10000000000)                      # Sentinel 2
    i = 0
    j = 0
    for x in range(p,r+1):             # because we know there are total r - p + 1 elements which is = len(A)
        if L[i] <= R[j]:                # compare each element of L and R and put smaller one in A an move its index forward
            A[x] = L[i]
            i += 1                      # move index forward
        else:
            A[x] = R[j]
            j += 1

def mergesort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

arr = [85,24,63,45,17,31,96,50]
mergesort(arr,0,len(arr)-1)
print(arr)


