# =============================================================================================================================
# SEARCHING (BINARY SEARCH) — COMPLETE PROBLEM SET  (~60 problems)
# Progress: Easy [0/16] | Medium [0/32] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Patterns: Classic BS | Finding Boundaries | BS on Rotated/Modified Array | BS on Answer Space | 2D BS
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (16 problems) — Build the binary search muscle memory
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Classic binary search — return index of target in sorted array, or -1.
# Input:  arr=[-1,0,3,5,9,12], target=9  →  Output: 4
# Input:  arr=[-1,0,3,5,9,12], target=2  →  Output: -1

def binarySearch(arr, target):
    pass

# print(binarySearch([-1,0,3,5,9,12], 9))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Search insert position — return index where target is, or where it would be inserted.
# Input:  arr=[1,3,5,6], target=5  →  Output: 2
# Input:  arr=[1,3,5,6], target=2  →  Output: 1
# Input:  arr=[1,3,5,6], target=7  →  Output: 4

def searchInsert(arr, target):
    pass

# print(searchInsert([1,3,5,6], 2))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Floor of a number — largest element in array that is <= target.
# Input:  arr=[1,2,8,10,11,12,19], target=5  →  Output: 2
# Input:  arr=[1,2,8,10,11,12,19], target=20 →  Output: 19

def floorOfNumber(arr, target):
    pass

# print(floorOfNumber([1,2,8,10,11,12,19], 5))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Ceil of a number — smallest element in array that is >= target.
# Input:  arr=[1,2,8,10,11,12,19], target=5  →  Output: 8
# Input:  arr=[1,2,8,10,11,12,19], target=8  →  Output: 8

def ceilOfNumber(arr, target):
    pass

# print(ceilOfNumber([1,2,8,10,11,12,19], 5))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# First occurrence of target in sorted array.
# Input:  arr=[2,4,6,6,6,9], target=6  →  Output: 2
# Input:  arr=[2,4,6,6,6,9], target=5  →  Output: -1

def firstOccurrence(arr, target):
    pass

# print(firstOccurrence([2,4,6,6,6,9], 6))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Last occurrence of target in sorted array.
# Input:  arr=[2,4,6,6,6,9], target=6  →  Output: 4

def lastOccurrence(arr, target):
    pass

# print(lastOccurrence([2,4,6,6,6,9], 6))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Count occurrences of target in sorted array.
# Input:  arr=[1,2,2,2,3,4], target=2  →  Output: 3

def countOccurrences(arr, target):
    pass

# print(countOccurrences([1,2,2,2,3,4], 2))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Integer square root — return floor(sqrt(x)) without using sqrt().
# Input:  x=8   →  Output: 2  (sqrt(8) = 2.82...)
# Input:  x=4   →  Output: 2

def mySqrt(x):
    pass

# print(mySqrt(8))


# [E-09] -----------------------------------------------------------------------------------------------------------------------
# First bad version — given n versions, find first bad one (API: isBadVersion(v) → bool).
# Input:  n=5, bad=4  →  Output: 4

def firstBadVersion(n):
    # assume isBadVersion(version) is available
    pass


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Find smallest letter greater than target in a circular sorted list.
# Input:  letters=["c","f","j"], target="a"  →  Output: "c"
# Input:  letters=["c","f","j"], target="d"  →  Output: "f"
# Input:  letters=["c","f","j"], target="j"  →  Output: "c"  (wraps around)

def nextGreatestLetter(letters, target):
    pass

# print(nextGreatestLetter(["c","f","j"], "d"))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Guess number higher or lower — binary search on a number guessing game.
# Input:  n=10, pick=6  →  Output: 6

def guessNumber(n):
    # assume guess(num) returns -1, 0, or 1
    pass


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Count negative numbers in a sorted matrix (each row sorted descending).
# Input:  [[-3,2],[-1,3],[3,4],[5,6]]  →  Output: 1
# Input:  [[3,2],[1,0]]                →  Output: 0

def countNegatives(grid):
    pass

# print(countNegatives([[-3,2],[-1,3],[3,4],[5,6]]))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Arrange coins — find max number of complete rows you can place with n coins.
# Row k needs k coins. Total = k*(k+1)/2 <= n.
# Input:  n=5   →  Output: 2  (rows 1 and 2, 3rd incomplete)
# Input:  n=8   →  Output: 3

def arrangeCoins(n):
    pass

# print(arrangeCoins(8))


# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Find target in an infinite sorted array (API: reader.get(index)).
# Strategy: exponentially expand search space, then binary search.
# Input:  arr=[1,3,5,9,11,...], target=9  →  Output: 3

def searchInInfiniteArray(arr, target):
    pass

# print(searchInInfiniteArray([1,3,5,9,11,14,17], 9))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Minimum difference element — find element in sorted array closest to target.
# Input:  arr=[1,3,8,10,15], target=12  →  Output: 10

def minDiffElement(arr, target):
    pass

# print(minDiffElement([1,3,8,10,15], 12))


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Find position of an element in sorted array of infinite size with unknown length.
# Return index of target, -1 if not found.
# Input:  arr=[1,2,3,4,5,6,7,8,9,10], target=7  →  Output: 6

def findInUnknownSize(arr, target):
    pass

# print(findInUnknownSize([1,2,3,4,5,6,7,8,9,10], 7))


# =============================================================================================================================
# MEDIUM (32 problems) — Rotated Arrays | Finding Boundaries | BS on Answer | 2D BS
# =============================================================================================================================

# ----- FINDING BOUNDARIES / VARIATIONS (10 problems) ------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Find first and last position of element in sorted array.
# Input:  arr=[5,7,7,8,8,10], target=8  →  Output: [3,4]
# Input:  arr=[5,7,7,8,8,10], target=6  →  Output: [-1,-1]

def searchRange(arr, target):
    pass

# print(searchRange([5,7,7,8,8,10], 8))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Find peak element — element greater than its neighbours (multiple peaks possible, return any).
# Input:  [1,2,3,1]  →  Output: 2  (index of peak)
# Input:  [1,2,1,3,5,6,4]  →  Output: 1 or 5

def findPeakElement(nums):
    pass

# print(findPeakElement([1,2,3,1]))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Single element in a sorted array — every element appears twice except one. Find it in O(log n).
# Input:  [1,1,2,3,3,4,4,8,8]  →  Output: 2
# Input:  [3,3,7,7,10,11,11]   →  Output: 10

def singleNonDuplicate(nums):
    pass

# print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Find kth missing positive number in sorted array.
# Input:  arr=[2,3,4,7,11], k=5  →  Output: 9

def findKthMissing(arr, k):
    pass

# print(findKthMissing([2,3,4,7,11], 5))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# H-index — find max h such that h papers have at least h citations.
# Input:  citations=[3,0,6,1,5]  →  Output: 3

def hIndex(citations):
    pass

# print(hIndex([3,0,6,1,5]))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Find number of 1s in a sorted binary array (all 1s come after 0s).
# Input:  [0,0,1,1,1,1]  →  Output: 4

def countOnesInBinaryArray(arr):
    pass

# print(countOnesInBinaryArray([0,0,1,1,1,1]))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Find the index of the first 1 in a sorted binary array.
# Input:  [0,0,0,1,1,1]  →  Output: 3
# Input:  [1,1,1,1]      →  Output: 0

def firstOneIndex(arr):
    pass

# print(firstOneIndex([0,0,0,1,1,1]))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Find the square root to a given precision using binary search on real numbers.
# Input:  x=50, precision=3  →  Output: 7.071

def sqrtPrecision(x, precision):
    pass

# print(sqrtPrecision(50, 3))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Find the nth root of a number using binary search.
# Input:  n=3, m=27  →  Output: 3  (cube root of 27)

def nthRoot(n, m):
    pass

# print(nthRoot(3, 27))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Count occurrences of a number in a sorted array with duplicates (O(log n)).
# Input:  arr=[1,1,2,2,2,3], target=2  →  Output: 3

def countInSorted(arr, target):
    pass

# print(countInSorted([1,1,2,2,2,3], 2))


# ----- ROTATED / MODIFIED SORTED ARRAY (8 problems) -------------------------------------------------------------------------

# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Search in rotated sorted array (no duplicates).
# Input:  arr=[4,5,6,7,0,1,2], target=0  →  Output: 4
# Input:  arr=[4,5,6,7,0,1,2], target=3  →  Output: -1

def searchRotated(arr, target):
    pass

# print(searchRotated([4,5,6,7,0,1,2], 0))


# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Search in rotated sorted array II (with duplicates) — return True/False.
# Input:  arr=[2,5,6,0,0,1,2], target=0  →  Output: True
# Input:  arr=[2,5,6,0,0,1,2], target=3  →  Output: False

def searchRotatedII(arr, target):
    pass

# print(searchRotatedII([2,5,6,0,0,1,2], 0))


# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Find minimum in rotated sorted array (no duplicates).
# Input:  [3,4,5,1,2]  →  Output: 1
# Input:  [4,5,6,7,0,1,2]  →  Output: 0

def findMinRotated(nums):
    pass

# print(findMinRotated([3,4,5,1,2]))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Find minimum in rotated sorted array II (with duplicates).
# Input:  [2,2,2,0,1]  →  Output: 0

def findMinRotatedII(nums):
    pass

# print(findMinRotatedII([2,2,2,0,1]))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Find rotation count — how many times was the sorted array rotated?
# Input:  [4,5,6,7,0,1,2]  →  Output: 4  (index of minimum)

def findRotationCount(arr):
    pass

# print(findRotationCount([4,5,6,7,0,1,2]))


# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Find an element in a nearly sorted array (each element may be shifted ±1 position).
# Input:  arr=[10,3,40,20,50,80,70], target=40  →  Output: 2

def findInNearlySorted(arr, target):
    pass

# print(findInNearlySorted([10,3,40,20,50,80,70], 40))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Search in bitonic array — array increases then decreases. Find target.
# Input:  arr=[1,3,8,12,4,2], target=4  →  Output: 4  (index)

def searchBitonic(arr, target):
    pass

# print(searchBitonic([1,3,8,12,4,2], 4))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Find peak in bitonic (mountain) array — index of the maximum element.
# Input:  [0,1,0]          →  Output: 1
# Input:  [0,2,1,0]        →  Output: 1
# Input:  [1,3,5,4,2]      →  Output: 2

def peakIndexMountain(arr):
    pass

# print(peakIndexMountain([1,3,5,4,2]))


# ----- BINARY SEARCH ON ANSWER SPACE (10 problems) ---------------------------------------------------------------------------
# Core idea: instead of searching in an array, binary search over the possible answers.
# lo = min possible answer, hi = max possible answer.
# Write a check(mid) function that returns True/False.

# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Koko eating bananas — min eating speed k to finish all piles in h hours.
# Input:  piles=[3,6,7,11], h=8  →  Output: 4

def minEatingSpeed(piles, h):
    pass

# print(minEatingSpeed([3,6,7,11], 8))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Capacity to ship packages in D days — min ship capacity to ship all weights within D days.
# Input:  weights=[1,2,3,4,5,6,7,8,9,10], days=5  →  Output: 15

def shipWithinDays(weights, days):
    pass

# print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))


# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Minimum days to make m bouquets — each bouquet needs k adjacent bloomed flowers.
# Input:  bloomDay=[1,10,3,10,2], m=3, k=1  →  Output: 3

def minDaysBouquets(bloomDay, m, k):
    pass

# print(minDaysBouquets([1,10,3,10,2], 3, 1))


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Find the smallest divisor given a threshold — smallest divisor so sum of ceil(n/d) <= threshold.
# Input:  nums=[1,2,5,9], threshold=6  →  Output: 5

def smallestDivisor(nums, threshold):
    pass

# print(smallestDivisor([1,2,5,9], 6))


# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Aggressive cows — place k cows in stalls to maximise minimum distance between any two cows.
# Input:  stalls=[1,2,4,8,9], k=3  →  Output: 3

def aggressiveCows(stalls, k):
    pass

# print(aggressiveCows([1,2,4,8,9], 3))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Book allocation — allocate books to m students minimising maximum pages any student reads.
# Input:  books=[12,34,67,90], m=2  →  Output: 113

def allocateBooks(books, m):
    pass

# print(allocateBooks([12,34,67,90], 2))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Painter's partition — split boards among k painters minimising maximum work for any painter.
# Input:  boards=[10,20,30,40], k=2  →  Output: 60

def paintersPartition(boards, k):
    pass

# print(paintersPartition([10,20,30,40], 2))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Split array largest sum — split array into k subarrays minimising the largest subarray sum.
# Input:  nums=[7,2,5,10,8], k=2  →  Output: 18

def splitArrayLargestSum(nums, k):
    pass

# print(splitArrayLargestSum([7,2,5,10,8], 2))


# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Magnetic force between two balls — m balls in n positions, maximise minimum distance.
# Input:  position=[1,2,3,4,7], m=3  →  Output: 3

def maxDistance(position, m):
    pass

# print(maxDistance([1,2,3,4,7], 3))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# Minimum speed to arrive on time — min integer speed to reach office within given hours.
# Input:  dist=[1,3,2], hour=6  →  Output: 1

def minSpeedOnTime(dist, hour):
    pass

# print(minSpeedOnTime([1,3,2], 6))


# ----- 2D BINARY SEARCH (4 problems) -----------------------------------------------------------------------------------------

# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Search in a 2D matrix (fully sorted — treat as 1D array).
# Input:  matrix=[[1,3,5],[7,9,11],[13,15,17]], target=9  →  Output: True

def searchMatrix2D(matrix, target):
    pass

# print(searchMatrix2D([[1,3,5],[7,9,11],[13,15,17]], 9))


# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Search in 2D matrix II (rows and cols independently sorted — staircase search).
# Input:  matrix=[[1,4,7],[2,5,8],[3,6,9]], target=5  →  Output: True

def searchMatrixII(matrix, target):
    pass

# print(searchMatrixII([[1,4,7],[2,5,8],[3,6,9]], 5))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest element in a sorted matrix.
# Input:  matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8  →  Output: 13

def kthSmallestMatrix(matrix, k):
    pass

# print(kthSmallestMatrix([[1,5,9],[10,11,13],[12,13,15]], 8))


# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Row with maximum 1s in sorted binary matrix — each row is sorted (0s then 1s).
# Input:  [[0,0,1,1],[0,1,1,1],[0,0,0,1],[0,0,0,0]]  →  Output: 1

def rowMaxOnes(matrix):
    pass

# print(rowMaxOnes([[0,0,1,1],[0,1,1,1],[0,0,0,1],[0,0,0,0]]))


# =============================================================================================================================
# HARD (12 problems) — Advanced BS on answer, real-valued BS, multi-dimensional
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Median of two sorted arrays — find median in O(log(min(m,n))).
# Input:  nums1=[1,3], nums2=[2]        →  Output: 2.0
# Input:  nums1=[1,2], nums2=[3,4]      →  Output: 2.5

def findMedianSortedArrays(nums1, nums2):
    pass

# print(findMedianSortedArrays([1,3], [2]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest pair distance — kth smallest distance among all pairs in array.
# Input:  nums=[1,3,1], k=1  →  Output: 0

def smallestDistancePair(nums, k):
    pass

# print(smallestDistancePair([1,3,1], 1))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Find kth smallest in multiplication table — kth smallest in m×n table where table[i][j]=i*j.
# Input:  m=3, n=3, k=5  →  Output: 3

def findKthInMultiplicationTable(m, n, k):
    pass

# print(findKthInMultiplicationTable(3, 3, 5))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Minimize max distance to gas station — add k stations to minimise max gap between stations.
# Input:  stations=[1,2,3,4,5,6,7,8,9,10], k=9  →  Output: 0.5

def minMaxGasStation(stations, k):
    pass

# print(minMaxGasStation([1,2,3,4,5,6,7,8,9,10], 9))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest in union of sorted arrays.
# Input:  arrays=[[1,3,5],[2,4,6],[7,8]], k=5  →  Output: 5

def kthSmallestUnion(arrays, k):
    pass

# print(kthSmallestUnion([[1,3,5],[2,4,6],[7,8]], 5))


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# Count of range sum — count range sums that lie in [lower, upper].
# Input:  nums=[-2,5,-1], lower=-2, upper=2  →  Output: 3

def countRangeSum(nums, lower, upper):
    pass

# print(countRangeSum([-2,5,-1], -2, 2))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Minimum number of days to disconnect island — NOT a BS problem but tests recognising when BS doesn't apply.
# Think: can binary search work here? Why or why not?
# Input:  grid=[[0,1,1,0],[0,1,1,0],[0,0,0,0]]  →  Output: 2

def minDaysDisconnect(grid):
    pass

# print(minDaysDisconnect([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Swim in rising water — minimum time to travel (0,0) to (n-1,n-1) as water rises.
# Binary search on time + BFS to check feasibility.
# Input:  [[0,2],[1,3]]  →  Output: 3

def swimInRisingWater(grid):
    pass

# print(swimInRisingWater([[0,2],[1,3]]))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# Maximum average subarray II — find contiguous subarray of length >= k with max average.
# Input:  nums=[1,12,-5,-6,50,3], k=4  →  Output: 12.75

def findMaxAverage(nums, k):
    pass

# print(findMaxAverage([1,12,-5,-6,50,3], 4))


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Weighted job scheduling — max profit by selecting non-overlapping jobs.
# Binary search for last non-conflicting job + DP.
# Input:  jobs=[(1,3,50),(3,5,20),(0,6,100),(5,9,200)]  →  Output: 250

def weightedJobScheduling(jobs):
    pass

# print(weightedJobScheduling([(1,3,50),(3,5,20),(0,6,100),(5,9,200)]))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Cutting ribbons — cut ribbons to get k pieces, maximise each piece length.
# Input:  ribbons=[9,7,5], k=3  →  Output: 5

def maxLength(ribbons, k):
    pass

# print(maxLength([9,7,5], 3))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Maximum number of tasks you can assign — assign tasks to workers given pills that boost strength.
# Input:  tasks=[3,2,1], workers=[0,3,3], pills=1, strength=1  →  Output: 3

def maxTaskAssign(tasks, workers, pills, strength):
    pass

# print(maxTaskAssign([3,2,1], [0,3,3], 1, 1))
