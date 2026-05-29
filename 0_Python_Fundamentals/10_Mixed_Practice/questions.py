# =============================================================================================================================
# MIXED PRACTICE — PROBLEM SET  (~14 problems)
# Progress: Easy [0/3] | Medium [0/6] | Hard [0/5]
#
# Daily target: 1 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
#
# This is your final checkpoint before DSA. These problems require you to:
# CHOOSE the right data structure, COMBINE techniques, and THINK before coding.
# If you can solve these comfortably → you're ready for 3_Array_Problems.
#
# Patterns: Loops + Dict | String + Stack | List + Set | Recursion + DP | Simulation
# =============================================================================================================================


# =============================================================================================================================
# EASY (3 problems) — Simple combinations of two concepts
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Given a list of integers, return a dict mapping each number to its square.
# Input:  [1,2,3,4,5]  →  Output: {1:1, 2:4, 3:9, 4:16, 5:25}

def squaresDict(nums):
    pass

# print(squaresDict([1,2,3,4,5]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Given a sentence, return the word that appears most frequently (case-insensitive).
# If tie, return the one that appears first.
# Input:  "the cat sat on the mat"  →  Output: "the"

def mostFrequentWord(sentence):
    pass

# print(mostFrequentWord("the cat sat on the mat"))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list of strings, return a list of only the palindromes.
# Input:  ["racecar","hello","level","world","madam"]  →  Output: ["racecar","level","madam"]

def filterPalindromes(words):
    pass

# print(filterPalindromes(["racecar","hello","level","world","madam"]))


# =============================================================================================================================
# MEDIUM (6 problems) — Loops + Dict | String + Stack | List + Set | Simulation
# =============================================================================================================================

# ----- LOOPS + DICT (2 problems) ---------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Roman numeral to integer. I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
# If a smaller value precedes a larger, subtract it.
# Input:  "III"     →  Output: 3
# Input:  "IV"      →  Output: 4
# Input:  "MCMXCIV" →  Output: 1994

def romanToInt(s):
    pass

# print(romanToInt("III"))
# print(romanToInt("IV"))
# print(romanToInt("MCMXCIV"))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Given a paragraph and a list of banned words, return the most frequent non-banned word.
# Ignore punctuation and case.
# Input:  "Bob hit a ball, the hit BALL flew far after it was hit", banned=["hit"]
# Output: "ball"

def mostCommonWord(paragraph, banned):
    pass

# print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit", ["hit"]))


# ----- STRING + LIST (2 problems) --------------------------------------------------------------------------------------------

# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Given a string of digits, return the number of ways to decode it.
# Mapping: 'A'=1, 'B'=2, ..., 'Z'=26. "0" or leading zero → invalid.
# Input:  "12"   →  Output: 2   ("AB" or "L")
# Input:  "226"  →  Output: 3   ("BZ","VF","BBF")
# Input:  "06"   →  Output: 0   (invalid)

def decodeWays(s):
    pass

# print(decodeWays("12"))
# print(decodeWays("226"))
# print(decodeWays("06"))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Given an m x n grid, count all unique paths from top-left to bottom-right,
# moving only right or down. Solve iteratively using a 2D list.
# Input:  m=3, n=7  →  Output: 28

def uniquePaths(m, n):
    pass

# print(uniquePaths(3, 7))
# print(uniquePaths(3, 3))


# ----- SIMULATION (2 problems) -----------------------------------------------------------------------------------------------

# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Given an n x n matrix, return the sum of the main diagonal plus the anti-diagonal.
# Don't double-count the center element for odd n.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: 25   (1+5+9 + 3+5+7 - 5)

def diagonalSum(matrix):
    pass

# print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
# print(diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Given a list of words and a window size, return all anagram windows.
# An anagram window is a contiguous sublist of words that together form an anagram of all words.
# Simpler version: Given s and p, find all start indices of p's anagrams in s.
# Input:  s="cbaebabacd", p="abc"  →  Output: [0, 6]

def findAnagrams(s, p):
    pass

# print(findAnagrams("cbaebabacd", "abc"))


# =============================================================================================================================
# HARD (5 problems) — Multi-technique, closest to real interview problems
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Arrange numbers in a list to form the largest possible number. Return as string.
# Input:  [3,30,34,5,9]   →  Output: "9534330"
# Input:  [10,2]          →  Output: "210"
# Input:  [0,0]           →  Output: "0"

def largestNumber(nums):
    pass

# print(largestNumber([3,30,34,5,9]))
# print(largestNumber([10,2]))
# print(largestNumber([0,0]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Return all combinations of n pairs of balanced parentheses using backtracking.
# Input:  3  →  Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

def generateParentheses(n):
    pass

# print(sorted(generateParentheses(3)))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Given a string, find the length of the longest substring that contains at most 2 distinct characters.
# Input:  "eceba"   →  Output: 3   ("ece")
# Input:  "ccaabbb" →  Output: 5   ("aabbb")

def longestTwoDistinct(s):
    pass

# print(longestTwoDistinct("eceba"))
# print(longestTwoDistinct("ccaabbb"))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Trapping Rain Water — given heights of bars, compute how much water can be trapped.
# Use two-pointer approach.
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]  →  Output: 6
# Input:  [4,2,0,3,2,5]              →  Output: 9

def trapRainWater(height):
    pass

# print(trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trapRainWater([4,2,0,3,2,5]))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Word break — can string s be segmented into words from wordDict?
# Input:  s="leetcode",     wordDict=["leet","code"]        →  Output: True
# Input:  s="applepenapple",wordDict=["apple","pen"]        →  Output: True
# Input:  s="catsandog",    wordDict=["cats","dog","sand"]  →  Output: False

def wordBreak(s, wordDict):
    pass

# print(wordBreak("leetcode", ["leet","code"]))
# print(wordBreak("applepenapple", ["apple","pen"]))
# print(wordBreak("catsandog", ["cats","dog","sand"]))
