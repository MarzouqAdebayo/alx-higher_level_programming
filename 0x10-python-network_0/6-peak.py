#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""

def find_peak(nums):
    """
    Return a peak in a list of unsorted integers
    """
    if len(nums) == 0:
        return None
    i = 0
    j = len(nums) - 1
    peak = 0
    while (i < j):
        if nums[i] > peak:
            peak = nums[i]
        if nums[j] > peak:
            peak = nums[j]
        i+=1
        j-=1
    return peak
