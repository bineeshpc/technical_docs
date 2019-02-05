# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

""" Minimum number of jumps to reach end
Given an array of integers where each element represents the max number of steps that
 can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array 
(starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.
"""

import sys
infinity = sys.maxsize

def all_reachable(a, start):
    max_jump_possible = a[start]
    for i in range(1, max_jump_possible+1):
        position = start + i
        if position < len(a):
            yield position

def minimum_jumps(a, start, end):
    """
    minumum of all positions reachable from start for all 
    positions reachable from start
    """
    if start == end:
        return 0
    minimum = infinity

    for position in all_reachable(a, start):
        minimum = 1 + min(minimum, minimum_jumps(a, position, end))
    return minimum
            

def minimum_jumps_top_down_dp(a, start, end):
    n = len(a)
    jumps = []
    for i in range(n):
        jump = []
        for j in range(n):
            jump.append(False)
        jumps.append(jump)
        
    def minimum_jumps(a, start, end):
        if start == end:
            return 0
        if jumps[start][end]:
            return jumps[start][end]
        minimum = infinity
        for position in all_reachable(a, start):
            minimum = 1 + min(minimum, minimum_jumps(a, position, end))
        jumps[start][end] = minimum
        return jumps[start][end]
    return minimum_jumps(a, start, end)



a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minimum_jumps(a, 0, len(a) - 1))
print(minimum_jumps_top_down_dp(a, 0, len(a)-1))
