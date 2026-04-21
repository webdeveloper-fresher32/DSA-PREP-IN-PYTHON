# =============================================================================================================================
# ARRAYS — COMPLETE PROBLEM SET  (~75 problems)
# Progress: Easy [0/22] | Medium [0/41] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (22 problems) — Basics, loops, variable tracking
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Reverse an array in-place.
# Input:  [1, 4, 3, 2, 6, 5]  →  Output: [5, 6, 2, 3, 4, 1]

def reverseArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# print(reverseArray([1, 4, 3, 2, 6, 5]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Find the minimum and maximum elements in the array.
# Input:  [3, 5, 4, 1, 9]  →  Output: [1, 9]

def minAndMax(arr):
    mini, maxi = arr[0], arr[0]
    for x in arr:
        if x < mini: mini = x
        if x > maxi: maxi = x
    return [mini, maxi]

# print(minAndMax([3, 5, 4, 1, 9]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Check if an array is sorted in non-decreasing order.
# Input:  [1, 2, 3, 4, 5]  →  Output: True
# Input:  [1, 3, 2, 4, 5]  →  Output: False

def isSorted(arr):
    for x in arr:
        if arr[x] < arr[x+1]: return True 
        else:
            return False

# print(isSorted([1, 2,3 , 4, 5]))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Count the frequency of each element.
# Input:  [1, 2, 1, 3, 2, 1]  →  Output: {1: 3, 2: 2, 3: 1}

def countFrequency(arr):
    newdict={}
    for i in range(len(arr)):
        if arr[i] in newdict:
            newdict[arr[i]]+=1
        else :
            newdict[arr[i]]=1
    return newdict


# print(countFrequency([4, 7, 2, 4, 9, 7, 2, 4, 5, 9, 1, 2, 7, 5, 4, 3, 2, 9, 8, 1, 5, 6, 3, 7, 2, 4, 6, 8, 9, 1]))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Find the second largest element (no duplicates counted).
# Input:  [12, 35, 1, 10, 34, 1]  →  Output: 34

def secondLargest(arr):
    n = len(arr)-1
    first=float("-inf")
    secnd=float("-inf")
    for i in range(n):
        if arr[i] > first :
            first=arr[i]
        if arr[i] < first: 
            secnd=arr[i]
    return secnd



# print(secondLargest([12, 35, 1, 10, 34, 1]))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Left rotate the array by one position.
# Input:  [1, 2, 3, 4, 5]  →  Output: [2, 3, 4, 5, 1]

def leftRotateByOne(arr):
    return arr[1:]+arr[:1]

# print(leftRotateByOne([1, 2, 3, 4, 5]))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Left rotate the array by k positions.
# Input:  [1, 2, 3, 4, 5], k=2  →  Output: [3, 4, 5, 1, 2]

def leftRotateByK(arr, k):
    return arr[k:]+arr[:k]

# print(leftRotateByK([1, 2, 3, 4, 5], 2))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Linear search — return the index of target, or -1 if not found.
# Input:  [4, 2, 7, 1, 9], target=7  →  Output: 2

def linearSearch(arr, target):
    n=len(arr)-1
    for i in range(n):
        if target == arr[i]:
            return i
    return -1


# print(linearSearch([4, 2, 7, 1, 9], 7))


# [E-09] -----------------------------------------------------------------------------------------------------------------------
# Find the missing number in an array of 1 to n.
# Input:  [1, 2, 4, 5, 6]  →  Output: 3

def missingNumber(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2
    
    cal_sum = sum(arr)
    
    return total_sum - cal_sum

# print(missingNumber([1, 2, 4, 5, 6]))


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Find the single number — every element appears twice except one. ( need to use bit manipulation for this kind of probelms )
# Input:  [4, 1, 2, 1, 2]  →  Output: 4

# best solution 
# | Approach | Time | Space  |
# | -------- | ---- | ------ |
# | HashMap  | O(n) | O(n)   |
# | XOR      | O(n) | O(1) ✅ |

# def singleNumber(arr):
#     result = 0
#     for num in arr:
#         result ^= num
#     return result

# print(singleNumber([4, 1, 2, 1, 2]))  # Output: 4

# explanation is
# = 4 ^ (1 ^ 1) ^ (2 ^ 2)
# = 4 ^ 0 ^ 0
# = 4

def singleNumber(arr):
    n=len(arr)
    newdict={}
    for i in range(n):
        if arr[i] in newdict:
            newdict[arr[i]]+=1
        else:
            newdict[arr[i]]=1
    return [key for key,val in newdict.items() if val==1]

# print(singleNumber([4, 1, 2, 1, 2]))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Contains duplicate — return True if any element appears more than once.
# Input:  [1, 2, 3, 1]  →  Output: True
# Input:  [1, 2, 3, 4]  →  Output: False

def containsDuplicate(arr):
    seen=set()
    for x in arr:
        if x in seen :
            return True
        seen.add(x)
    return False

# print(containsDuplicate([1, 2, 3, 1]))


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Move all zeros to the end, maintaining order of non-zero elements.
# Input:  [0, 1, 0, 3, 12]  →  Output: [1, 3, 12, 0, 0]

def moveZeros(arr):
    pass

print(moveZeros([0, 1, 0, 3, 12]))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Remove duplicates from a sorted array in-place. Return count of unique elements.
# Input:  [1, 1, 2, 2, 3]  →  Output: 3

def removeDuplicatesSorted(arr):
    pass

# print(removeDuplicatesSorted([1, 1, 2, 2, 3]))


# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Plus one — treat array as a number, add 1.
# Input:  [1, 2, 3]  →  Output: [1, 2, 4]
# Input:  [9, 9, 9]  →  Output: [1, 0, 0, 0]

def plusOne(arr):
    pass

# print(plusOne([9, 9, 9]))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Best time to buy and sell stock (one transaction only). Return max profit.
# Input:  [7, 1, 5, 3, 6, 4]  →  Output: 5  (buy at 1, sell at 6)

def maxProfit(prices):
    pass

# print(maxProfit([7, 1, 5, 3, 6, 4]))


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Maximum subarray sum (Kadane's algorithm).
# Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]  →  Output: 6  (subarray [4,-1,2,1])

def maxSubarraySum(arr):
    pass

# print(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# [E-17] -----------------------------------------------------------------------------------------------------------------------
# Union of two sorted arrays (no duplicates in result).
# Input:  [1, 2, 4, 5], [2, 3, 5, 6]  →  Output: [1, 2, 3, 4, 5, 6]

def unionSorted(a, b):
    pass

# print(unionSorted([1, 2, 4, 5], [2, 3, 5, 6]))


# [E-18] -----------------------------------------------------------------------------------------------------------------------
# Intersection of two sorted arrays (only common elements).
# Input:  [1, 2, 4, 5], [2, 4, 6]  →  Output: [2, 4]

def intersectionSorted(a, b):
    pass

# print(intersectionSorted([1, 2, 4, 5], [2, 4, 6]))


# [E-19] -----------------------------------------------------------------------------------------------------------------------
# Pascal's triangle — return the nth row (0-indexed).
# Input:  n=4  →  Output: [1, 4, 6, 4, 1]

def pascalRow(n):
    pass

# print(pascalRow(4))


# [E-20] -----------------------------------------------------------------------------------------------------------------------
# Find all numbers that appear twice in an array of range [1, n].
# Input:  [4, 3, 2, 7, 8, 2, 3, 1]  →  Output: [2, 3]

def findDuplicates(arr):
    pass

# print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


# [E-21] -----------------------------------------------------------------------------------------------------------------------
# Majority element — element that appears more than n//2 times (guaranteed to exist).
# Input:  [3, 2, 3]  →  Output: 3
# Input:  [2, 2, 1, 1, 1, 2, 2]  →  Output: 2

def majorityElement(arr):
    pass

# print(majorityElement([2, 2, 1, 1, 1, 2, 2]))


# [E-22] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest element in an unsorted array.
# Input:  [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k=4  →  Output: 5

def kthSmallest(arr, k):
    pass

# print(kthSmallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4))


# =============================================================================================================================
# MEDIUM (41 problems) — Two Pointers | Sliding Window | Hashing | Prefix Sum | Mixed
# =============================================================================================================================

# ----- TWO POINTERS (10 problems) --------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Pair sum in sorted array — check if any two elements sum to target.
# Input:  [1, 2, 3, 4, 6], target=6  →  Output: True  (2+4)
# Input:  [1, 2, 3, 9], target=8     →  Output: False

def pairSumSorted(arr, target):
    pass

# print(pairSumSorted([1, 2, 3, 4, 6], 6))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Two sum (unsorted) — return indices of two numbers that add up to target.
# Input:  [2, 7, 11, 15], target=9  →  Output: [0, 1]
# Input:  [3, 2, 4], target=6       →  Output: [1, 2]

def twoSum(arr, target):
    pass

# print(twoSum([2, 7, 11, 15], 9))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Three sum — find all unique triplets that sum to zero.
# Input:  [-1, 0, 1, 2, -1, -4]  →  Output: [[-1, -1, 2], [-1, 0, 1]]

def threeSum(arr):
    pass

# print(threeSum([-1, 0, 1, 2, -1, -4]))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Container with most water — find two lines that together hold the most water.
# Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]  →  Output: 49

def maxWater(height):
    pass

# print(maxWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Sort colors (Dutch National Flag) — sort array of 0s, 1s, 2s in-place.
# Input:  [2, 0, 2, 1, 1, 0]  →  Output: [0, 0, 1, 1, 2, 2]

def sortColors(arr):
    pass

# print(sortColors([2, 0, 2, 1, 1, 0]))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Four sum — find all unique quadruplets that sum to target.
# Input:  [1, 0, -1, 0, -2, 2], target=0  →  Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

def fourSum(arr, target):
    pass

# print(fourSum([1, 0, -1, 0, -2, 2], 0))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Remove element in-place — remove all occurrences of val.
# Input:  [3, 2, 2, 3], val=3  →  Output: 2 (array becomes [2, 2, ...])

def removeElement(arr, val):
    pass

# print(removeElement([3, 2, 2, 3], 3))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Merge sorted arrays — merge arr2 into arr1 in-place (arr1 has extra space).
# Input:  arr1=[1,2,3,0,0,0], m=3, arr2=[2,5,6], n=3  →  Output: [1,2,2,3,5,6]

def mergeSortedArrays(arr1, m, arr2, n):
    pass

# print(mergeSortedArrays([1,2,3,0,0,0], 3, [2,5,6], 3))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Find the duplicate number — array of n+1 integers in range [1, n], exactly one duplicate.
# Input:  [1, 3, 4, 2, 2]  →  Output: 2

def findDuplicate(arr):
    pass

# print(findDuplicate([1, 3, 4, 2, 2]))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Rearrange array by sign — place positives and negatives alternately (equal count guaranteed).
# Input:  [3, 1, -2, -5, 2, -4]  →  Output: [3, -2, 1, -5, 2, -4]

def rearrangeBySign(arr):
    pass

# print(rearrangeBySign([3, 1, -2, -5, 2, -4]))


# ----- SLIDING WINDOW (10 problems) ------------------------------------------------------------------------------------------

# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum of any contiguous subarray of size k.
# Input:  [2, 1, 5, 1, 3, 2], k=3  →  Output: 9  ([5,1,3])

def maxSumSubarrayK(arr, k):
    pass

# print(maxSumSubarrayK([2, 1, 5, 1, 3, 2], 3))


# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Longest subarray with sum equal to k (can have negatives).
# Input:  [1, -1, 5, -2, 3], k=3  →  Output: 4  ([1,-1,5,-2])

def longestSubarraySumK(arr, k):
    pass

# print(longestSubarraySumK([1, -1, 5, -2, 3], 3))


# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Minimum size subarray with sum >= target (all positives).
# Input:  [2, 3, 1, 2, 4, 3], target=7  →  Output: 2  ([4,3])

def minSizeSubarraySum(arr, target):
    pass

# print(minSizeSubarraySum([2, 3, 1, 2, 4, 3], 7))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Longest substring without repeating characters.
# Input:  "abcabcbb"  →  Output: 3  ("abc")
# Input:  "bbbbb"     →  Output: 1  ("b")

def lengthOfLongestSubstring(s):
    pass

# print(lengthOfLongestSubstring("abcabcbb"))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Fruits into baskets — max fruits you can pick with exactly 2 types of fruit.
# Input:  [1, 2, 1, 2, 3]  →  Output: 4  ([1,2,1,2])

def fruitsIntoBaskets(arr):
    pass

# print(fruitsIntoBaskets([1, 2, 1, 2, 3]))


# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Longest subarray with at most k distinct elements.
# Input:  [1, 2, 1, 2, 3], k=2  →  Output: 4

def longestSubarrayKDistinct(arr, k):
    pass

# print(longestSubarrayKDistinct([1, 2, 1, 2, 3], 2))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Number of subarrays with product less than k.
# Input:  [10, 5, 2, 6], k=100  →  Output: 8

def numSubarraysProductLessThanK(arr, k):
    pass

# print(numSubarraysProductLessThanK([10, 5, 2, 6], 100))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Longest repeating character replacement — replace at most k characters to get longest same-char substring.
# Input:  "AABABBA", k=1  →  Output: 4

def characterReplacement(s, k):
    pass

# print(characterReplacement("AABABBA", 1))


# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Maximum number of vowels in a substring of length k.
# Input:  "abciiidef", k=3  →  Output: 3  ("iii")

def maxVowelsInWindow(s, k):
    pass

# print(maxVowelsInWindow("abciiidef", 3))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Count number of nice subarrays — subarrays with exactly k odd numbers.
# Input:  [1, 1, 2, 1, 1], k=3  →  Output: 2

def numberOfSubarrays(arr, k):
    pass

# print(numberOfSubarrays([1, 1, 2, 1, 1], 3))


# ----- HASHING (11 problems) -------------------------------------------------------------------------------------------------

# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Subarray with zero sum — check if any subarray sums to zero.
# Input:  [4, 2, -3, 1, 6]  →  Output: True  ([2,-3,1])
# Input:  [1, 2, 3]         →  Output: False

def subarrayWithZeroSum(arr):
    pass

# print(subarrayWithZeroSum([4, 2, -3, 1, 6]))


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Longest subarray with equal 0s and 1s (binary array).
# Input:  [0, 1, 0, 1, 1, 1, 0]  →  Output: 6

def longestEqualZeroOne(arr):
    pass

# print(longestEqualZeroOne([0, 1, 0, 1, 1, 1, 0]))


# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Count subarrays with sum equal to k.
# Input:  [1, 2, 3], k=3  →  Output: 2  ([1,2] and [3])

def subarraysSumK(arr, k):
    pass

# print(subarraysSumK([1, 2, 3], 3))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Find all pairs with a given difference d.
# Input:  [1, 5, 3, 4, 2], d=3  →  Output: [(1,4), (2,5)]

def pairsWithDiff(arr, d):
    pass

# print(pairsWithDiff([1, 5, 3, 4, 2], 3))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Top k frequent elements.
# Input:  [1, 1, 1, 2, 2, 3], k=2  →  Output: [1, 2]

def topKFrequent(arr, k):
    pass

# print(topKFrequent([1, 1, 1, 2, 2, 3], 2))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Group anagrams — group strings that are anagrams of each other.
# Input:  ["eat","tea","tan","ate","nat","bat"]  →  Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

def groupAnagrams(strs):
    pass

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Longest consecutive sequence — find length of longest sequence of consecutive integers.
# Input:  [100, 4, 200, 1, 3, 2]  →  Output: 4  ([1,2,3,4])

def longestConsecutive(arr):
    pass

# print(longestConsecutive([100, 4, 200, 1, 3, 2]))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# Count pairs with given sum (unsorted, count all pairs including duplicates).
# Input:  [1, 5, 7, -1, 5], target=6  →  Output: 3

def countPairsWithSum(arr, target):
    pass

# print(countPairsWithSum([1, 5, 7, -1, 5], 6))


# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Find the first non-repeating element in the array.
# Input:  [9, 4, 9, 6, 7, 4]  →  Output: 6

def firstNonRepeating(arr):
    pass

# print(firstNonRepeating([9, 4, 9, 6, 7, 4]))


# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Subarray with given sum (only positive numbers) — return start and end indices.
# Input:  [1, 4, 20, 3, 10, 5], target=33  →  Output: (2, 4)

def subarrayWithGivenSum(arr, target):
    pass

# print(subarrayWithGivenSum([1, 4, 20, 3, 10, 5], 33))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Four sum count — count tuples (i,j,k,l) such that A[i]+B[j]+C[k]+D[l] == 0.
# Input:  A=[1,2], B=[-2,-1], C=[-1,2], D=[0,2]  →  Output: 2

def fourSumCount(A, B, C, D):
    pass

# print(fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))


# ----- PREFIX SUM (6 problems) -----------------------------------------------------------------------------------------------

# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Range sum query — answer multiple queries [l, r] on a static array.
# Input:  arr=[1,3,5,7,9,11], queries=[(1,3),(0,5)]  →  Output: [15, 36]

def rangeSumQuery(arr, queries):
    pass

# print(rangeSumQuery([1,3,5,7,9,11], [(1,3),(0,5)]))


# [M-33] -----------------------------------------------------------------------------------------------------------------------
# Equilibrium index — index where left sum equals right sum.
# Input:  [1, 7, 3, 6, 5, 6]  →  Output: 3

def equilibriumIndex(arr):
    pass

# print(equilibriumIndex([1, 7, 3, 6, 5, 6]))


# [M-34] -----------------------------------------------------------------------------------------------------------------------
# Product of array except self (no division allowed).
# Input:  [1, 2, 3, 4]  →  Output: [24, 12, 8, 6]

def productExceptSelf(arr):
    pass

# print(productExceptSelf([1, 2, 3, 4]))


# [M-35] -----------------------------------------------------------------------------------------------------------------------
# Count subarrays with equal number of 0s and 1s (prefix sum approach).
# Input:  [0, 0, 1, 1, 0]  →  Output: 6

def countEqualZeroOne(arr):
    pass

# print(countEqualZeroOne([0, 0, 1, 1, 0]))


# [M-36] -----------------------------------------------------------------------------------------------------------------------
# Number of subarrays with sum in range [lower, upper].
# Input:  [2, 2, 0, 0, 0, 1, 1], lower=1, upper=2  →  Output: 14

def subarraysSumInRange(arr, lower, upper):
    pass

# print(subarraysSumInRange([2, 2, 0, 0, 0, 1, 1], 1, 2))


# [M-37] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum circular subarray.
# Input:  [5, -3, 5]  →  Output: 10
# Input:  [3, -1, 2, -1]  →  Output: 4

def maxCircularSubarraySum(arr):
    pass

# print(maxCircularSubarraySum([5, -3, 5]))


# ----- MIXED MEDIUM (4 problems) ---------------------------------------------------------------------------------------------

# [M-38] -----------------------------------------------------------------------------------------------------------------------
# Next permutation — rearrange to the next lexicographically greater permutation.
# Input:  [1, 2, 3]  →  Output: [1, 3, 2]
# Input:  [3, 2, 1]  →  Output: [1, 2, 3]

def nextPermutation(arr):
    pass

# print(nextPermutation([1, 2, 3]))


# [M-39] -----------------------------------------------------------------------------------------------------------------------
# Merge intervals — merge all overlapping intervals.
# Input:  [[1,3],[2,6],[8,10],[15,18]]  →  Output: [[1,6],[8,10],[15,18]]

def mergeIntervals(intervals):
    pass

# print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))


# [M-40] -----------------------------------------------------------------------------------------------------------------------
# Jump game — can you reach the last index?
# Input:  [2, 3, 1, 1, 4]  →  Output: True
# Input:  [3, 2, 1, 0, 4]  →  Output: False

def canJump(arr):
    pass

# print(canJump([2, 3, 1, 1, 4]))


# [M-41] -----------------------------------------------------------------------------------------------------------------------
# Set matrix zeroes — if element is 0, set its entire row and column to 0 in-place.
# Input:  [[1,1,1],[1,0,1],[1,1,1]]  →  Output: [[1,0,1],[0,0,0],[1,0,1]]

def setZeroes(matrix):
    pass

# print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))


# =============================================================================================================================
# HARD (12 problems) — Stretch your thinking, pick selectively
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Trapping Rain Water — how much water can be trapped between heights?
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]  →  Output: 6

def trap(height):
    pass

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Minimum window substring — smallest window in s containing all chars of t.
# Input:  s="ADOBECODEBANC", t="ABC"  →  Output: "BANC"

def minWindow(s, t):
    pass

# print(minWindow("ADOBECODEBANC", "ABC"))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Median of two sorted arrays — find median in O(log(m+n)).
# Input:  [1,3], [2]  →  Output: 2.0
# Input:  [1,2], [3,4]  →  Output: 2.5

def findMedianSortedArrays(nums1, nums2):
    pass

# print(findMedianSortedArrays([1,3], [2]))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Largest rectangle in histogram.
# Input:  [2,1,5,6,2,3]  →  Output: 10

def largestRectangleHistogram(heights):
    pass

# print(largestRectangleHistogram([2,1,5,6,2,3]))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Maximum product subarray.
# Input:  [2,3,-2,4]   →  Output: 6
# Input:  [-2,0,-1]    →  Output: 0

def maxProduct(arr):
    pass

# print(maxProduct([2,3,-2,4]))


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# First missing positive — smallest positive integer not in the array.
# Input:  [1,2,0]   →  Output: 3
# Input:  [3,4,-1,1]  →  Output: 2

def firstMissingPositive(arr):
    pass

# print(firstMissingPositive([3,4,-1,1]))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Count inversions — count pairs (i, j) where i < j but arr[i] > arr[j].
# Input:  [2, 4, 1, 3, 5]  →  Output: 3

def countInversions(arr):
    pass

# print(countInversions([2, 4, 1, 3, 5]))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Merge k sorted arrays into one sorted array.
# Input:  [[1,4,5],[1,3,4],[2,6]]  →  Output: [1,1,2,3,4,4,5,6]

def mergeKSortedArrays(arrays):
    pass

# print(mergeKSortedArrays([[1,4,5],[1,3,4],[2,6]]))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# Sliding window maximum — max in every window of size k.
# Input:  [1,3,-1,-3,5,3,6,7], k=3  →  Output: [3,3,5,5,6,7]

def slidingWindowMaximum(arr, k):
    pass

# print(slidingWindowMaximum([1,3,-1,-3,5,3,6,7], 3))


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Longest subarray with absolute difference <= limit.
# Input:  [8,2,4,7], limit=4  →  Output: 2

def longestSubarrayLimit(arr, limit):
    pass

# print(longestSubarrayLimit([8,2,4,7], 4))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum of two non-overlapping subarrays of lengths L and M.
# Input:  [0,6,5,2,2,5,1,9,4], L=1, M=2  →  Output: 20

def maxSumTwoNoOverlap(arr, L, M):
    pass

# print(maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Shortest subarray with sum >= k (can have negatives) — use deque + prefix sum.
# Input:  [2,-1,2], k=3  →  Output: 3

def shortestSubarraySum(arr, k):
    pass

# print(shortestSubarraySum([2,-1,2], 3))
