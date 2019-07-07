"""Highly inefficient exponential time solution for rod cutting problem"""

# If we draw the recursion tree for n = 4 as shown pn page 364 CLRS, we see that same function
# is called multiple times example Cut_Rod(P,2) is called 2 times and Cut_Rod(P,1) is called
# 4 times. All these repeated calls result in exponential time because all 2^n-1 combinations
# are tried to get the best possible revenue. If we store the values of Cut_Rod(P,2) and Cut_Rod(P,1)
# we can avoid these repeated calls. We can instead check for these values in the storage array.
# If they already exist, then just pick value from that array instead of making a new recursive call
# This technique is called memoization. It has been implemented in next program which reduces time from 
# exponential to polynomial

def Cut_Rod(P,n):       # n = length of rod, P = array of prices for each inch
    if n == 0:
        return 0
    q = -10000000000000000
    for i in range(1,n+1):
        q = max(q,P[i] + Cut_Rod(P,n-i))    # If a rod of length i has been cut, then we just need to cut the remaining rod of length n-i. That is why P[i] is directly taken to be price because it has not be cut further. But revenue for left out rod of length n-1 is calculated recursively
    return q

arr = [1,5,8,9,10,17,17,20,24,30]

print('Answer :',Cut_Rod(arr,3))