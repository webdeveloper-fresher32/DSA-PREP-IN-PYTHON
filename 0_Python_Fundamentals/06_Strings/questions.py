# =============================================================================================================================
# STRINGS — PYTHON FUNDAMENTALS PROBLEM SET  (~14 problems)
# Progress: Easy [0/5] | Medium [0/6] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Patterns: Basic Manipulation | Searching | Hashing | Stack | Two Pointers
# =============================================================================================================================


# =============================================================================================================================
# EASY (5 problems) — Character manipulation, basic string methods
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Count vowels (a, e, i, o, u) in a string (case-insensitive).
# Input:  "Hello World"  →  Output: 3

def countVowels(s):
    pass

# print(countVowels("Hello World"))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Reverse the order of words in a sentence (not the characters).
# Input:  "Hello World"    →  Output: "World Hello"
# Input:  "I love Python"  →  Output: "Python love I"

def reverseWords(s):
    pass

# print(reverseWords("Hello World"))
# print(reverseWords("I love Python"))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Shift each letter by k positions (Caesar cipher). Wrap around. Keep case. Leave non-letters unchanged.
# Input:  "Hello, World!", k=3  →  Output: "Khoor, Zruog!"

def caesarCipher(s, k):
    pass

# print(caesarCipher("Hello, World!", 3))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Compress consecutive repeated characters with character + count.
# If compressed string is not shorter than original, return original.
# Input:  "aabcccdddd"  →  Output: "a2b1c3d4"
# Input:  "abc"         →  Output: "abc"

def compressString(s):
    pass

# print(compressString("aabcccdddd"))
# print(compressString("abc"))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Return a dict of character frequencies (ignore spaces).
# Input:  "hello"  →  Output: {"h":1, "e":1, "l":2, "o":1}

def charFrequency(s):
    pass

# print(charFrequency("hello"))


# =============================================================================================================================
# MEDIUM (6 problems) — Hashing | Two Pointers | Stack
# =============================================================================================================================

# ----- HASHING (3 problems) --------------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Return True if s1 and s2 are anagrams (ignore spaces and case).
# Input:  "listen", "silent"  →  Output: True
# Input:  "hello", "world"    →  Output: False

def isAnagram(s1, s2):
    pass

# print(isAnagram("listen", "silent"))
# print(isAnagram("hello", "world"))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Return the index of the first character that appears only once. Return -1 if none.
# Input:  "leetcode"  →  Output: 0   ('l')
# Input:  "aabb"      →  Output: -1

def firstUniqueChar(s):
    pass

# print(firstUniqueChar("leetcode"))
# print(firstUniqueChar("aabb"))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Return the length of the longest substring with all unique characters.
# Input:  "abcabcbb"  →  Output: 3   ("abc")
# Input:  "bbbbb"     →  Output: 1   ("b")

def longestUniqueSubstring(s):
    pass

# print(longestUniqueSubstring("abcabcbb"))
# print(longestUniqueSubstring("bbbbb"))


# ----- TWO POINTERS / STACK (3 problems) -------------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Return True if brackets are balanced and closed in the correct order.
# Valid chars: (, ), {, }, [, ]
# Input:  "()[]{}"  →  Output: True
# Input:  "([)]"    →  Output: False
# Input:  "{[]}"    →  Output: True

def validParentheses(s):
    pass

# print(validParentheses("()[]{}"))
# print(validParentheses("([)]"))
# print(validParentheses("{[]}"))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Return the longest palindromic substring. If multiple of same length, return first.
# Input:  "babad"  →  Output: "bab"
# Input:  "cbbd"   →  Output: "bb"

def longestPalindrome(s):
    pass

# print(longestPalindrome("babad"))
# print(longestPalindrome("cbbd"))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Return True if s1 and s2 are isomorphic (characters in s1 can map one-to-one to s2).
# Input:  "egg",   "add"   →  Output: True    (e→a, g→d)
# Input:  "foo",   "bar"   →  Output: False   (o can't map to both a and r)
# Input:  "paper", "title" →  Output: True

def isIsomorphic(s1, s2):
    pass

# print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("paper", "title"))


# =============================================================================================================================
# HARD (3 problems) — Multi-step string problems
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Decode a string like "3[a]2[bc]" → "aaabcbc", "3[a2[c]]" → "accaccacc".
# The number before brackets means repeat the contents that many times.

def decodeString(s):
    pass

# print(decodeString("3[a]2[bc]"))
# print(decodeString("3[a2[c]]"))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Minimum window substring — find the smallest window in s containing all characters of t.
# Input:  s="ADOBECODEBANC", t="ABC"  →  Output: "BANC"
# Input:  s="a", t="a"                →  Output: "a"

def minWindow(s, t):
    pass

# print(minWindow("ADOBECODEBANC", "ABC"))
# print(minWindow("a", "a"))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list of words, group all anagrams together.
# Input:  ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]  (order within groups doesn't matter)

def groupAnagrams(words):
    pass

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
