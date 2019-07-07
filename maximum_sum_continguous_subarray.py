"""Author - Anantvir Singh, concept reference:= CLRS"""
"""Maximum Subarray is a very simple and smart application of divide and conquer for stock prediction i.e which buy and sell dates yield maximum profit. 
It is helpful only if there are some negative values in array because if all values are positive then maximum subarray is sum
of entire array !, For detailed analysis refer to CLRS page 70"""

# The subarray must be contiguous

import math
def max_crossing_subarray(A,low,mid,high):         # Max subarray can lie in left half od passed array A, right half of A, or it can cross the mid point with index starting from i<=mid and ending index j >=mid
    left_sum = -10000000000                             # Negative infinity
    sum = 0
    for i in range(mid+1,low,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -10000000000
    sum = 0
    for j in range(mid+1,high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left,max_right,left_sum + right_sum)

def maximum_sum_contiguous_subarray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid = math.floor((low + high)/2)
        left_low,left_high,left_sum = maximum_sum_contiguous_subarray(A,low,mid)
        right_low,right_high,right_sum = maximum_sum_contiguous_subarray(A,mid+1,high)
        cross_low,cross_high, cross_sum = max_crossing_subarray(A,low,mid,high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low,left_high,left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low,right_high,right_sum
        else:
            return cross_low,cross_high,cross_sum

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print(maximum_sum_contiguous_subarray(arr,0,len(arr)-1))


