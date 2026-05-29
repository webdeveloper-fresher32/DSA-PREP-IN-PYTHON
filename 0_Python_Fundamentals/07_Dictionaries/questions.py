# =============================================================================================================================
# DICTIONARIES (HASHMAPS) — PROBLEM SET  (~14 problems)
# Progress: Easy [0/4] | Medium [0/7] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Key insight: dicts turn O(n²) brute-force into O(n) — frequency, grouping, lookup
# Patterns: Frequency Counting | Grouping | Prefix Hashmap | Two-Pass
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Basic dict operations and frequency counting
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Given a sentence, return a dict of word frequencies (case-insensitive).
# Input:  "the cat sat on the mat"  →  Output: {"the":2,"cat":1,"sat":1,"on":1,"mat":1}

def wordCount(sentence):
    pass

# print(wordCount("the cat sat on the mat"))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Given a dict, return a new dict with keys and values swapped. Assume values are unique.
# Input:  {"a":1, "b":2, "c":3}  →  Output: {1:"a", 2:"b", 3:"c"}

def invertDict(d):
    pass

# print(invertDict({"a":1, "b":2, "c":3}))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Return the element that appears most often in the list. If tie, return the one appearing first.
# Input:  [1, 3, 2, 3, 1, 1]  →  Output: 1

def mostFrequent(nums):
    pass

# print(mostFrequent([1, 3, 2, 3, 1, 1]))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Return the index of the first character that appears only once in the string. Return -1 if none.
# Input:  "leetcode"  →  Output: 0   ('l')
# Input:  "aabb"      →  Output: -1

def firstUniqueChar(s):
    pass

# print(firstUniqueChar("leetcode"))
# print(firstUniqueChar("aabb"))


# =============================================================================================================================
# MEDIUM (7 problems) — Two-Pass | Prefix Hashmap | Grouping | Advanced Lookup
# =============================================================================================================================

# ----- FREQUENCY & GROUPING (3 problems) -------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Group anagrams — group strings that are anagrams of each other. Use sorted key.
# Input:  ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

def groupAnagrams(strs):
    pass

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Return the k most frequent elements. Order doesn't matter.
# Input:  [1,1,1,2,2,3], k=2  →  Output: [1, 2]

def topKFrequent(nums, k):
    pass

# print(topKFrequent([1,1,1,2,2,3], 2))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Sort a list of integers by frequency (most frequent first).
# For equal frequency, sort by value ascending.
# Input:  [1,1,2,2,2,3]   →  Output: [2,2,2,1,1,3]
# Input:  [2,3,1,3,2]     →  Output: [2,2,3,3,1]

def frequencySort(nums):
    pass

# print(frequencySort([1,1,2,2,2,3]))
# print(frequencySort([2,3,1,3,2]))


# ----- PREFIX HASHMAP (2 problems) -------------------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Two Sum using hashmap — O(n) solution. Return indices of two numbers that sum to target.
# Input:  [2,7,11,15], target=9  →  Output: [0, 1]
# Input:  [3,2,4],     target=6  →  Output: [1, 2]

def twoSum(nums, target):
    pass

# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Count subarrays whose sum equals k using prefix sum + hashmap. Solve in O(n).
# Input:  [1,1,1], k=2  →  Output: 2
# Input:  [1,2,3], k=3  →  Output: 2

def subarraySumK(nums, k):
    pass

# print(subarraySumK([1,1,1], 2))
# print(subarraySumK([1,2,3], 3))


# ----- TWO-PASS / ADVANCED LOOKUP (2 problems) -------------------------------------------------------------------------------

# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Return True if s1 and s2 are isomorphic (chars in s1 map one-to-one to s2).
# Input:  "egg",  "add"  →  Output: True
# Input:  "foo",  "bar"  →  Output: False

def isIsomorphic(s1, s2):
    pass

# print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Word pattern — does string s follow the same pattern as pattern string?
# Input:  pattern="abba", s="dog cat cat dog"   →  Output: True
# Input:  pattern="abba", s="dog cat cat fish"  →  Output: False

def wordPattern(pattern, s):
    pass

# print(wordPattern("abba", "dog cat cat dog"))
# print(wordPattern("abba", "dog cat cat fish"))


# =============================================================================================================================
# HARD (3 problems) — Consecutive sequences, multi-map, advanced grouping
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Find the longest consecutive integer sequence in O(n) using a set.
# Only start counting from the beginning of a sequence (num-1 not in set).
# Input:  [100,4,200,1,3,2]  →  Output: 4   (sequence: 1,2,3,4)

def longestConsecutive(nums):
    pass

# print(longestConsecutive([100,4,200,1,3,2]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Given a paragraph and a list of banned words, return the most frequent non-banned word.
# Ignore case and punctuation.
# Input:  "Bob hit a ball, the hit BALL flew far after it was hit", banned=["hit"]
# Output: "ball"

def mostCommonWord(paragraph, banned):
    pass

# print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit", ["hit"]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list of strings, find the longest common prefix.
# Input:  ["flower","flow","flight"]  →  Output: "fl"
# Input:  ["dog","racecar","car"]     →  Output: ""

def longestCommonPrefix(strs):
    pass

# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
