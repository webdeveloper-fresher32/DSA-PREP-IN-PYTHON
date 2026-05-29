# =============================================================================================================================
# LISTS — PROBLEM SET  (~14 problems)
# Progress: Easy [0/5] | Medium [0/6] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Patterns: Basic Operations | Two Pointers | Sliding Window | Prefix
# =============================================================================================================================


# =============================================================================================================================
# EASY (5 problems) — Indexing, slicing, basic list operations
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Reverse a list WITHOUT using .reverse() or [::-1].
# Input:  [1, 2, 3, 4, 5]  →  Output: [5, 4, 3, 2, 1]

def reverseList(nums):
    pass

# print(reverseList([1, 2, 3, 4, 5]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Remove duplicates from a list, preserving first-occurrence order.
# Input:  [1, 3, 2, 3, 1, 4]  →  Output: [1, 3, 2, 4]

def removeDuplicates(nums):
    pass

# print(removeDuplicates([1, 3, 2, 3, 1, 4]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Split a list into chunks of size k. Last chunk may be smaller.
# Input:  [1,2,3,4,5,6,7], k=3  →  Output: [[1,2,3],[4,5,6],[7]]

def chunkList(nums, k):
    pass

# print(chunkList([1,2,3,4,5,6,7], 3))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Merge two sorted lists into one sorted list. Do NOT use sort() — compare elements.
# Input:  [1,3,5], [2,4,6]  →  Output: [1,2,3,4,5,6]

def mergeSorted(a, b):
    pass

# print(mergeSorted([1,3,5], [2,4,6]))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Flatten a list one level deep (sublists within sublists stay nested).
# Input:  [[1,2],[3,[4,5]],6]  →  Output: [1,2,3,[4,5],6]

def flattenOneLevel(nested):
    pass

# print(flattenOneLevel([[1,2],[3,[4,5]],6]))


# =============================================================================================================================
# MEDIUM (6 problems) — Two Pointers | Sliding Window | Prefix Sum
# =============================================================================================================================

# ----- TWO POINTERS (2 problems) ---------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Rotate a list to the right by k positions.
# Input:  [1,2,3,4,5], k=2  →  Output: [4,5,1,2,3]

def rotateRight(nums, k):
    pass

# print(rotateRight([1,2,3,4,5], 2))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Two Sum — return the indices of two numbers that add up to target.
# Use a hashmap to solve in O(n). Assume exactly one solution.
# Input:  [2,7,11,15], target=9  →  Output: [0, 1]
# Input:  [3,2,4],     target=6  →  Output: [1, 2]

def twoSum(nums, target):
    pass

# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))


# ----- SLIDING WINDOW (2 problems) -------------------------------------------------------------------------------------------

# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list and window size k, return the max sum of each window of size k.
# Input:  [2,1,5,1,3,2], k=3  →  Output: [8, 7, 9, 6]

def slidingWindowMaxSum(nums, k):
    pass

# print(slidingWindowMaxSum([2,1,5,1,3,2], 3))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Find the maximum subarray sum (Kadane's Algorithm).
# Input:  [-2,1,-3,4,-1,2,1,-5,4]  →  Output: 6   (subarray [4,-1,2,1])
# Input:  [1]                       →  Output: 1

def maxSubarraySum(nums):
    pass

# print(maxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))


# ----- PREFIX SUM (2 problems) -----------------------------------------------------------------------------------------------

# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Product of array except self — output[i] = product of all elements except nums[i].
# Do NOT use division.
# Input:  [1,2,3,4]  →  Output: [24,12,8,6]

def productExceptSelf(nums):
    pass

# print(productExceptSelf([1,2,3,4]))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Count the number of subarrays whose sum equals k.
# Input:  [1,1,1], k=2  →  Output: 2
# Input:  [1,2,3], k=3  →  Output: 2

def subarraySumK(nums, k):
    pass

# print(subarraySumK([1,1,1], 2))
# print(subarraySumK([1,2,3], 3))


# =============================================================================================================================
# HARD (3 problems) — Multi-step, in-place, advanced patterns
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Given an unsorted list, return the length of the longest consecutive integer sequence.
# Solve in O(n) using a set — do not sort.
# Input:  [100,4,200,1,3,2]  →  Output: 4   (sequence: 1,2,3,4)

def longestConsecutive(nums):
    pass

# print(longestConsecutive([100,4,200,1,3,2]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Given a list of integers representing heights of bars, find two bars that together
# can hold the most water (container with most water). Return the max area.
# Input:  [1,8,6,2,5,4,8,3,7]  →  Output: 49

def maxWater(height):
    pass

# print(maxWater([1,8,6,2,5,4,8,3,7]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Find all unique triplets [a, b, c] such that a + b + c = 0.
# Sort the result. No duplicate triplets allowed.
# Input:  [-1,0,1,2,-1,-4]  →  Output: [[-1,-1,2],[-1,0,1]]
# Input:  [0,0,0]            →  Output: [[0,0,0]]

def threeSum(nums):
    pass

# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,0,0]))
