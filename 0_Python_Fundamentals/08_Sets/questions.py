# =============================================================================================================================
# SETS — PROBLEM SET  (~13 problems)
# Progress: Easy [0/4] | Medium [0/6] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Key insight: sets give O(1) "have I seen this?" — use them to eliminate nested loops
# Patterns: Uniqueness | Membership Testing | Set Operations | Cycle Detection
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Set basics and set operations
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Return a sorted list of elements that appear in BOTH lists.
# Input:  [1,2,3,4], [3,4,5,6]  →  Output: [3, 4]

def commonElements(a, b):
    pass

# print(commonElements([1,2,3,4], [3,4,5,6]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Return a tuple of two sorted lists: (elements only in a, elements only in b).
# Input:  [1,2,3,4], [3,4,5,6]  →  Output: ([1, 2], [5, 6])

def uniqueToEach(a, b):
    pass

# print(uniqueToEach([1,2,3,4], [3,4,5,6]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Return True if any value appears more than once. Solve in O(n) using a set.
# Input:  [1,2,3,1]  →  Output: True
# Input:  [1,2,3,4]  →  Output: False

def containsDuplicate(nums):
    pass

# print(containsDuplicate([1,2,3,1]))
# print(containsDuplicate([1,2,3,4]))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Return a list of all elements that appear more than once.
# Input:  [4,3,2,7,8,2,3,1]  →  Output: [2, 3]

def findDuplicates(nums):
    pass

# print(findDuplicates([4,3,2,7,8,2,3,1]))


# =============================================================================================================================
# MEDIUM (6 problems) — Membership lookups | Multi-set ops | Missing elements
# =============================================================================================================================

# ----- MEMBERSHIP & MISSING (3 problems) -------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Given a list of n distinct integers from 0 to n, return the one missing number.
# Use set difference — solve in O(n).
# Input:  [3,0,1]              →  Output: 2
# Input:  [9,6,4,2,3,5,7,0,1] →  Output: 8

def missingNumber(nums):
    pass

# print(missingNumber([3,0,1]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Return elements that appear in ALL of the given lists.
# Input:  [[1,2,3],[2,3,4],[2,5,3]]  →  Output: [2, 3]

def intersectAll(lists):
    pass

# print(sorted(intersectAll([[1,2,3],[2,3,4],[2,5,3]])))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Two sentences are similar if they have the exact same set of unique words (case-insensitive).
# Input:  "I love cats and dogs", "dogs love I cats and"  →  Output: True
# Input:  "hello world",          "world"                 →  Output: False

def sentencesSimilar(s1, s2):
    pass

# print(sentencesSimilar("I love cats and dogs", "dogs love I cats and"))
# print(sentencesSimilar("hello world", "world"))


# ----- CYCLE DETECTION & MATH (3 problems) -----------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Happy number: replace n with sum of squares of its digits. Repeat until n=1 (happy) or cycles (not happy).
# Use a set to detect the cycle.
# Input:  19  →  Output: True    (19→82→68→100→1)
# Input:  2   →  Output: False

def isHappy(n):
    pass

# print(isHappy(19))
# print(isHappy(2))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Longest consecutive sequence — O(n) using a set.
# Only start counting from the beginning of a sequence (num-1 not in set).
# Input:  [100,4,200,1,3,2]  →  Output: 4

def longestConsecutive(nums):
    pass

# print(longestConsecutive([100,4,200,1,3,2]))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Given two strings s and t where t is s with one extra character inserted at a random position,
# return that extra character. Use set/XOR or frequency approach.
# Input:  s="abcd", t="abcde"  →  Output: "e"
# Input:  s="",     t="y"      →  Output: "y"

def findExtraChar(s, t):
    pass

# print(findExtraChar("abcd", "abcde"))
# print(findExtraChar("", "y"))


# =============================================================================================================================
# HARD (3 problems) — Multi-set logic, longest sequences, complex lookups
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Given a list of words and a list of characters, find all words that can be formed
# by characters in the list (each character can be used only once per word).
# Return the total length of all such words.
# Input:  words=["cat","bt","hat","tree"], chars="atach"  →  Output: 6  ("cat"+"hat")

def countCharacters(words, chars):
    pass

# print(countCharacters(["cat","bt","hat","tree"], "atach"))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Find the first duplicate in an array — return the element that first repeats
# (i.e., whose second occurrence has the smallest index).
# Input:  [2,1,3,5,3,2]  →  Output: 3
# Input:  [2,4,3,5,1]    →  Output: -1   (no duplicates)

def firstDuplicate(nums):
    pass

# print(firstDuplicate([2,1,3,5,3,2]))
# print(firstDuplicate([2,4,3,5,1]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list of integers and a value k, return True if there are two distinct indices
# i and j such that nums[i] == nums[j] and abs(i - j) <= k.
# Input:  [1,2,3,1], k=3  →  Output: True
# Input:  [1,0,1,1], k=1  →  Output: True
# Input:  [1,2,3,1], k=0  →  Output: False

def containsNearbyDuplicate(nums, k):
    pass

# print(containsNearbyDuplicate([1,2,3,1], 3))
# print(containsNearbyDuplicate([1,2,3,1], 0))
