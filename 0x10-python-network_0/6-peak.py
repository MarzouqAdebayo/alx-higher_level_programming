#!/usr/bin/python3
def find_peak(nums):
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
