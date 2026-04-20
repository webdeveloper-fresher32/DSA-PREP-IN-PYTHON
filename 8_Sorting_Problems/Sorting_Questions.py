# =============================================================================================================================
# SORTING — COMPLETE PROBLEM SET  (~62 problems)
# Progress: Easy [0/16] | Medium [0/34] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Patterns: Sorting Algorithms | Custom Comparator | Merge Sort Based | Quick Select | Counting/Bucket | Sort + Greedy
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (16 problems) — Algorithm implementations + basic sort-based problems
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Implement bubble sort.
# Input:  [64,34,25,12,22,11,90]  →  Output: [11,12,22,25,34,64,90]

def bubbleSort(arr):
    pass

# print(bubbleSort([64,34,25,12,22,11,90]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Implement selection sort.
# Input:  [64,25,12,22,11]  →  Output: [11,12,22,25,64]

def selectionSort(arr):
    pass

# print(selectionSort([64,25,12,22,11]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Implement insertion sort.
# Input:  [12,11,13,5,6]  →  Output: [5,6,11,12,13]

def insertionSort(arr):
    pass

# print(insertionSort([12,11,13,5,6]))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Sort an array of 0s, 1s, and 2s in a single pass (Dutch National Flag).
# Input:  [2,0,2,1,1,0]  →  Output: [0,0,1,1,2,2]

def sortColors(arr):
    pass

# print(sortColors([2,0,2,1,1,0]))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Sort array by parity — all even numbers first, then odd.
# Input:  [3,1,2,4]  →  Output: [2,4,3,1]  (any valid order)

def sortByParity(arr):
    pass

# print(sortByParity([3,1,2,4]))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Squares of a sorted array — return sorted array of squares.
# Input:  [-4,-1,0,3,10]  →  Output: [0,1,9,16,100]

def sortedSquares(arr):
    pass

# print(sortedSquares([-4,-1,0,3,10]))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Sort array by increasing frequency. Tie-break: higher value first.
# Input:  [1,1,2,2,2,3]  →  Output: [3,1,1,2,2,2]

def frequencySort(arr):
    pass

# print(frequencySort([1,1,2,2,2,3]))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Relative sort array — sort arr1 so elements appear in the order given by arr2.
# Elements not in arr2 go at the end in ascending order.
# Input:  arr1=[2,3,1,3,2,4,3,3], arr2=[3,2]  →  Output: [3,3,3,3,2,2,1,4]

def relativeSortArray(arr1, arr2):
    pass

# print(relativeSortArray([2,3,1,3,2,4,3,3], [3,2]))


# [E-09] -----------------------------------------------------------------------------------------------------------------------
# Height checker — count students not standing in expected (sorted) order.
# Input:  [1,1,4,2,1,3]  →  Output: 3

def heightChecker(heights):
    pass

# print(heightChecker([1,1,4,2,1,3]))


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Third maximum number — return 3rd distinct maximum. If not exist, return maximum.
# Input:  [3,2,1]  →  Output: 1
# Input:  [1,2]    →  Output: 2

def thirdMax(nums):
    pass

# print(thirdMax([3,2,1]))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Minimum absolute difference — find all pairs with minimum absolute difference.
# Input:  [4,2,1,3]  →  Output: [[1,2],[2,3],[3,4]]

def minimumAbsDifference(arr):
    pass

# print(minimumAbsDifference([4,2,1,3]))


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Check if array is sorted and rotated.
# Input:  [3,4,5,1,2]  →  Output: True
# Input:  [2,1,3,4]    →  Output: False

def isSortedAndRotated(nums):
    pass

# print(isSortedAndRotated([3,4,5,1,2]))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Sort characters by frequency.
# Input:  "tree"   →  Output: "eert"  or  "eetr"
# Input:  "cccaaa" →  Output: "cccaaa" or "aaaccc"

def sortCharsByFrequency(s):
    pass

# print(sortCharsByFrequency("tree"))


# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Sort array after converting elements: if odd → add 1 to make even, if even → halve it. Then sort.
# Input:  [3,1,2,4]  →  Output: [2,2,2,4]  → sorted: [2,2,2,4]

def sortTransformed(arr):
    pass

# print(sortTransformed([3,1,2,4]))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Sort the people — sort names by their height in descending order.
# Input:  names=["Mary","John","Emma"], heights=[180,165,170]  →  Output: ["Mary","Emma","John"]

def sortPeople(names, heights):
    pass

# print(sortPeople(["Mary","John","Emma"], [180,165,170]))


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Sort array by digit sum — sort by the sum of digits of each element.
# Input:  [21,11,11,10,2]  →  Output: [10,2,11,11,21]  (sums: 3,2,2,1,3)

def sortByDigitSum(arr):
    pass

# print(sortByDigitSum([21,11,11,10,2]))


# =============================================================================================================================
# MEDIUM (34 problems) — Algorithms | Merge Sort Based | Quick Select | Custom Sort | Sort + Greedy
# =============================================================================================================================

# ----- SORTING ALGORITHM IMPLEMENTATIONS (5 problems) ------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Implement merge sort. Return sorted array.
# Input:  [38,27,43,3,9,82,10]  →  Output: [3,9,10,27,38,43,82]

def mergeSort(arr):
    pass

# print(mergeSort([38,27,43,3,9,82,10]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Implement quick sort. Return sorted array.
# Input:  [10,7,8,9,1,5]  →  Output: [1,5,7,8,9,10]

def quickSort(arr):
    pass

# print(quickSort([10,7,8,9,1,5]))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Implement heap sort. Return sorted array.
# Input:  [12,11,13,5,6,7]  →  Output: [5,6,7,11,12,13]

def heapSort(arr):
    pass

# print(heapSort([12,11,13,5,6,7]))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Implement counting sort (for non-negative integers with known range).
# Input:  arr=[4,2,2,8,3,3,1], max_val=8  →  Output: [1,2,2,3,3,4,8]

def countingSort(arr, max_val):
    pass

# print(countingSort([4,2,2,8,3,3,1], 8))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Implement radix sort (LSD, for non-negative integers).
# Input:  [170,45,75,90,802,24,2,66]  →  Output: [2,24,45,66,75,90,170,802]

def radixSort(arr):
    pass

# print(radixSort([170,45,75,90,802,24,2,66]))


# ----- MERGE SORT BASED (6 problems) -----------------------------------------------------------------------------------------

# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Count inversions in array — count pairs (i,j) where i<j but arr[i]>arr[j].
# Input:  [2,4,1,3,5]  →  Output: 3  (pairs: (2,1),(4,1),(4,3))

def countInversions(arr):
    pass

# print(countInversions([2,4,1,3,5]))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Merge k sorted arrays into one sorted array.
# Input:  [[1,4,5],[1,3,4],[2,6]]  →  Output: [1,1,2,3,4,4,5,6]

def mergeKSortedArrays(arrays):
    pass

# print(mergeKSortedArrays([[1,4,5],[1,3,4],[2,6]]))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Merge k sorted lists (linked list version — simulate with arrays here).
# Input:  [[1,4,5],[1,3,4],[2,6]]  →  Output: [1,1,2,3,4,4,5,6]

def mergeKSortedLists(lists):
    pass

# print(mergeKSortedLists([[1,4,5],[1,3,4],[2,6]]))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Sort a linked list using merge sort (simulate with array).
# Input:  [4,2,1,3]  →  Output: [1,2,3,4]

def sortLinkedList(arr):
    pass

# print(sortLinkedList([4,2,1,3]))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Count reverse pairs — count pairs (i,j) where i<j and arr[i] > 2*arr[j].
# Input:  [1,3,2,3,1]  →  Output: 2

def countReversePairs(arr):
    pass

# print(countReversePairs([1,3,2,3,1]))


# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Merge two sorted arrays without extra space — merge arr2 into arr1 in-place.
# Input:  arr1=[1,3,5,7], arr2=[0,2,6,8]  →  Output: arr1=[0,1,2,3], arr2=[5,6,7,8]

def mergeTwoSortedNoSpace(arr1, arr2):
    pass

# print(mergeTwoSortedNoSpace([1,3,5,7], [0,2,6,8]))


# ----- QUICK SELECT (4 problems) ----------------------------------------------------------------------------------------------

# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Kth largest element in an array — find in O(n) average using quick select.
# Input:  [3,2,1,5,6,4], k=2  →  Output: 5

def findKthLargest(nums, k):
    pass

# print(findKthLargest([3,2,1,5,6,4], 2))


# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest element in an unsorted array using quick select.
# Input:  [7,10,4,3,20,15], k=3  →  Output: 7

def findKthSmallest(nums, k):
    pass

# print(findKthSmallest([7,10,4,3,20,15], 3))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Top k frequent elements using quick select on frequency.
# Input:  [1,1,1,2,2,3], k=2  →  Output: [1,2]

def topKFrequent(nums, k):
    pass

# print(topKFrequent([1,1,1,2,2,3], 2))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Kth largest element in a stream — design a class that finds kth largest after each add().
# Input:  k=3, nums=[4,5,8,2], add(3)→4, add(5)→5, add(10)→5, add(9)→8, add(4)→8

class KthLargest:
    def __init__(self, k, nums):
        pass
    def add(self, val):
        pass

# kl = KthLargest(3, [4,5,8,2]); print([kl.add(x) for x in [3,5,10,9,4]])


# ----- CUSTOM COMPARATOR / CUSTOM SORT (7 problems) --------------------------------------------------------------------------

# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Largest number — arrange numbers to form the largest possible number.
# Input:  [3,30,34,5,9]  →  Output: "9534330"

def largestNumber(nums):
    pass

# print(largestNumber([3,30,34,5,9]))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Wiggle sort — arr[0] <= arr[1] >= arr[2] <= arr[3] ...
# Input:  [3,5,2,1,6,4]  →  Output: [3,5,1,6,2,4]  (one valid answer)

def wiggleSort(arr):
    pass

# print(wiggleSort([3,5,2,1,6,4]))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Sort array by power value — power = steps to reach 1 via Collatz conjecture. Tie-break by value.
# Input:  lo=12, hi=15, k=2  →  Output: 13

def getKthCollatz(lo, hi, k):
    pass

# print(getKthCollatz(12, 15, 2))


# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Sort students by exam score then by name alphabetically.
# Input:  students=[("Alice",85),("Bob",92),("Charlie",85)]  →  Output: [("Bob",92),("Alice",85),("Charlie",85)]

def sortStudents(students):
    pass

# print(sortStudents([("Alice",85),("Bob",92),("Charlie",85)]))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Reorder data in log files — letter-logs before digit-logs, letter-logs sorted lexicographically.
# Input:  ["dig1 8 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1","dig2 3 6"]

def reorderLogFiles(logs):
    pass

# print(reorderLogFiles(["dig1 8 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))


# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Maximum units on a truck — pick boxes to maximise units loaded given weight limit.
# Input:  boxTypes=[[1,3],[2,2],[3,1]], truckSize=4  →  Output: 8

def maximumUnits(boxTypes, truckSize):
    pass

# print(maximumUnits([[1,3],[2,2],[3,1]], 4))


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Sort integers by the number of 1s in their binary representation.
# Tie-break: smaller integer first.
# Input:  arr=[0,1,2,3,4,5,6,7,8]  →  Output: [0,1,2,4,8,3,5,6,7]

def sortByBits(arr):
    pass

# print(sortByBits([0,1,2,3,4,5,6,7,8]))


# ----- COUNTING / BUCKET SORT (4 problems) -----------------------------------------------------------------------------------

# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Maximum gap — find maximum difference between successive elements in sorted form.
# Must run in O(n) time using bucket/radix sort.
# Input:  [3,6,9,1]  →  Output: 3

def maximumGap(nums):
    pass

# print(maximumGap([3,6,9,1]))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Top k frequent words using bucket sort.
# Input:  words=["i","love","leetcode","i","love","coding"], k=2  →  Output: ["i","love"]

def topKFrequentWords(words, k):
    pass

# print(topKFrequentWords(["i","love","leetcode","i","love","coding"], 2))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Sort array with elements in range [1, n²] using counting sort (O(n)).
# Input:  arr=[4,1,9,16,25], n=5  →  Output: [1,4,9,16,25]

def sortInRange(arr, n):
    pass

# print(sortInRange([4,1,9,16,25], 5))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Find all duplicates in array of range [1,n] using bucket/index marking — O(n) time, O(1) space.
# Input:  [4,3,2,7,8,2,3,1]  →  Output: [2,3]

def findAllDuplicates(nums):
    pass

# print(findAllDuplicates([4,3,2,7,8,2,3,1]))


# ----- SORT + GREEDY (8 problems) --------------------------------------------------------------------------------------------

# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Merge intervals — merge all overlapping intervals.
# Input:  [[1,3],[2,6],[8,10],[15,18]]  →  Output: [[1,6],[8,10],[15,18]]

def mergeIntervals(intervals):
    pass

# print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# Non-overlapping intervals — remove minimum intervals to make rest non-overlapping.
# Input:  [[1,2],[2,3],[3,4],[1,3]]  →  Output: 1

def eraseOverlapIntervals(intervals):
    pass

# print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))


# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Meeting rooms II — minimum number of conference rooms required.
# Input:  intervals=[[0,30],[5,10],[15,20]]  →  Output: 2

def minMeetingRooms(intervals):
    pass

# print(minMeetingRooms([[0,30],[5,10],[15,20]]))


# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Minimum number of platforms — minimum platforms needed at a station.
# Input:  arrivals=[900,940,950,1100,1500,1800], departures=[910,1200,1120,1130,1900,2000]
# Output: 3

def minPlatforms(arrivals, departures):
    pass

# print(minPlatforms([900,940,950,1100,1500,1800], [910,1200,1120,1130,1900,2000]))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Activity selection — select maximum number of non-overlapping activities.
# Input:  start=[1,3,0,5,8,5], end=[2,4,6,7,9,9]  →  Output: 4

def activitySelection(start, end):
    pass

# print(activitySelection([1,3,0,5,8,5], [2,4,6,7,9,9]))


# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Two city scheduling — send n people to city A and n to city B, minimise total cost.
# Input:  costs=[[10,20],[30,200],[400,50],[30,20]]  →  Output: 110

def twoCityScheduling(costs):
    pass

# print(twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))


# [M-33] -----------------------------------------------------------------------------------------------------------------------
# Minimum cost to connect ropes — connect all ropes at minimum cost (each join costs sum of two lengths).
# Input:  ropes=[4,3,2,6]  →  Output: 29

def connectRopes(ropes):
    pass

# print(connectRopes([4,3,2,6]))


# [M-34] -----------------------------------------------------------------------------------------------------------------------
# Task scheduler — minimum intervals to finish all tasks with cooldown n between same tasks.
# Input:  tasks=["A","A","A","B","B","B"], n=2  →  Output: 8

def leastInterval(tasks, n):
    pass

# print(leastInterval(["A","A","A","B","B","B"], 2))


# =============================================================================================================================
# HARD (12 problems)
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Count of smaller numbers after self — for each element, count how many elements to its right are smaller.
# Use merge sort. Input: [5,2,6,1] → Output: [2,1,1,0]

def countSmaller(nums):
    pass

# print(countSmaller([5,2,6,1]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Reverse pairs — count pairs (i,j) where i<j and nums[i] > 2*nums[j].
# Input:  [1,3,2,3,1]  →  Output: 2

def reversePairs(nums):
    pass

# print(reversePairs([1,3,2,3,1]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Count of range sum — count range sums in [lower, upper] using merge sort.
# Input:  nums=[-2,5,-1], lower=-2, upper=2  →  Output: 3

def countRangeSum(nums, lower, upper):
    pass

# print(countRangeSum([-2,5,-1], -2, 2))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Sort a k-sorted (nearly sorted) array — each element is at most k positions away from its sorted position.
# Use a min-heap of size k+1. Input: arr=[6,5,3,2,8,10,9], k=3 → Output: [2,3,5,6,8,9,10]

def sortKSorted(arr, k):
    pass

# print(sortKSorted([6,5,3,2,8,10,9], 3))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Find median from a data stream — support addNum and findMedian operations.
# addNum(1), addNum(2), findMedian()→1.5, addNum(3), findMedian()→2.0

class MedianFinder:
    def __init__(self):
        pass
    def addNum(self, num):
        pass
    def findMedian(self):
        pass

# mf = MedianFinder(); mf.addNum(1); mf.addNum(2); print(mf.findMedian())


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# Sliding window median — find median of every window of size k.
# Input:  nums=[1,3,-1,-3,5,3,6,7], k=3  →  Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]

def slidingWindowMedian(nums, k):
    pass

# print(slidingWindowMedian([1,3,-1,-3,5,3,6,7], 3))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Minimum number of moves to sort — minimum swaps to sort array.
# Input:  [4,3,2,1]  →  Output: 2

def minSwapsToSort(arr):
    pass

# print(minSwapsToSort([4,3,2,1]))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Maximum performance of a team — pick at most k engineers maximising speed_sum * min_efficiency.
# Input:  n=6, speed=[2,10,3,1,5,8], efficiency=[5,4,3,9,7,2], k=2  →  Output: 60

def maxPerformance(n, speed, efficiency, k):
    pass

# print(maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# IPO — pick at most k projects to maximise capital, starting with initial capital w.
# Input:  k=2, w=0, profits=[1,2,3], capital=[0,1,1]  →  Output: 4

def findMaximizedCapital(k, w, profits, capital):
    pass

# print(findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Sort a matrix diagonally — sort each diagonal independently in ascending order.
# Input:  [[3,3,1,1],[2,2,1,2],[1,1,1,2]]  →  Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

def diagonalSortMatrix(mat):
    pass

# print(diagonalSortMatrix([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Minimum cost to hire k workers — pay each worker at least their expected wage/quality ratio.
# Input:  quality=[10,20,5], wage=[70,50,30], k=2  →  Output: 105.0

def mincostToHireWorkers(quality, wage, k):
    pass

# print(mincostToHireWorkers([10,20,5], [70,50,30], 2))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum of 3 non-overlapping subarrays — find 3 non-overlapping subarrays of size k with max sum.
# Input:  nums=[1,2,1,2,6,7,5,1], k=2  →  Output: [0,3,5]  (start indices)

def maxSumOfThreeSubarrays(nums, k):
    pass

# print(maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))
