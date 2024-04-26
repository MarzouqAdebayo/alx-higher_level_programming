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
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    mid = len(nums) // 2
    peak = nums[mid]
    if peak > nums[mid - 1] and peak > nums[mid + 1]:
        return peak
    elif peak < nums[mid - 1]:
        return find_peak(nums[:mid])
    else:
        return find_peak(nums[mid + 1:])
