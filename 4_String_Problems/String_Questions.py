# =============================================================================================================================
# STRINGS — COMPLETE PROBLEM SET  (~68 problems)
# Progress: Easy [0/18] | Medium [0/38] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Patterns: Sliding Window | Two Pointers | Hashing | Stack | DP
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (18 problems) — Basics, loops, character manipulation
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Reverse a string in-place.
# Input:  "hello"       →  Output: "olleh"
# Input:  "Hannah"      →  Output: "hannaH"

def reverseString(s):
    revStr=""
    for i in range(len(s)-1,-1,-1):
        revStr+=s[i]
    return revStr

# print(reverseString("Hannah"))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Check if a string is a palindrome (ignore case and non-alphanumeric).
# Input:  "A man, a plan, a canal: Panama"  →  Output: True
# Input:  "race a car"                      →  Output: False

def isPalindrome(s:str):
    # cleaned=""
    # for ch in s:
    #     if ch.isalnum():
    #         cleaned+=ch.lower()
    #     return cleaned==cleaned[::-1]

    first=0
    last=len(s)-1
    while first < last:
        print(s[first],s[last])
        while not s[first].isalnum():
            first+=1
        while not s[last].isalnum():
            last-=1
        if s[first].lower()!=s[last].lower():
            return False
        first+=1
        last-=1
    return True
# print(isPalindrome("Hello"))
# print(isPalindrome("A man, a plan, a canal: Panama"))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Count the number of vowels in a string.
# Input:  "hello world"  →  Output: 3

def countVowels(s):
    vowels=["a","e","i","o","u"]
    count=0
    for ch in s:
        if ch.lower() in vowels:
            count+=1
    return count

# print(countVowels("hello world"))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Check if two strings are anagrams of each other.
# Input:  "anagram", "nagaram"  →  Output: True
# Input:  "rat", "car"          →  Output: False

def isAnagram(s, t):
    return sorted(s)==sorted(t)

# print(isAnagram("anagram", "nagaram"))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Find the first non-repeating character in a string. Return its index, or -1.
# Input:  "leetcode"  →  Output: 0  ('l')
# Input:  "aabb"      →  Output: -1

def firstUniqChar(s):
    hasele={}
    for ch in s:
        if ch in hasele:
            hasele[ch]+=1
        else :
            hasele[ch]=1
    
    for index,ch in enumerate(s):
        if ch in hasele and hasele[ch] == 1:
            return index

# print(firstUniqChar("leetcode"))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Count occurrences of a character in a string.
# Input:  "hello", ch='l'  →  Output: 2

def countOccurrences(s, g):
   return s.count(g)

# print(countOccurrences("hello", 'l'))
# print(countOccurrences("mississippi", 's'))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Reverse the words in a string (words separated by spaces).
# Input:  "the sky is blue"   →  Output: "blue is sky the"
# Input:  "  hello world  "   →  Output: "world hello"

def reverseWords(s:str):
    newstr = s.split(" ")[::-1]
    return " ".join(newstr)


# print(reverseWords("the sky is blue"))
# print(reverseWords("  hello world  " ))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Remove duplicate characters from a string, keeping first occurrence.
# Input:  "geeksforgeeks"  →  Output: "geksfor"

def removeDuplicateChars(s:str):
    newstr=""
    seen=set()
    n=len(s)
    for i in range(n):
       if s[i] in seen:
           continue
       else :
          seen.add(s[i])
          newstr+=s[i]
    return newstr
           
  
# print(removeDuplicateChars("geeksforgeeks"))

# ==========================================Revision needed =============================================
# [E-09] ----------------------------------------------------------------------------------------------------------------------- ( REVISON NEEDED )
# Longest common prefix among a list of strings.
# Input:  ["flower","flow","flight"]  →  Output: "fl"
# Input:  ["dog","racecar","car"]     →  Output: ""

def longestCommonPrefix(s:list[str]):
    base=s[0]
    res=""
    for i in range(0,len(base)):
        for word in s[1:]:
            if i == len(word) or word[i] != base[i]:
                return res
        res+=base[i]
    return res

# print(longestCommonPrefix(["flower","flow","flight"]))


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Check if one string is a rotation of another.
# Input:  "abcde", "cdeab"  →  Output: True
# Input:  "abcde", "abced"  →  Output: False

def isRotation(s:str, t:str):
    n=len(s)
    i=0
    while i  < n:
        ch = s[:1]
        secnd = s[1:]+ch
        if secnd == t :
            return True 
        s=secnd
        i+=1
    return False

# print(isRotation("abcde", "cdeab"))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Implement atoi — convert string to integer (handle leading spaces, sign, overflow).
# Input:  "42"        →  Output: 42
# Input:  "  -42"     →  Output: -42
# Input:  "4193abc"   →  Output: 4193

def myAtoi(s):
    pass

# print(myAtoi("  -42"))


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Check if string contains only digits.
# Input:  "12345"   →  Output: True
# Input:  "123a5"   →  Output: False

def isAllDigits(s:str):
    for i in range(len(s)):
        if not s[i].isdigit():
            return False
    return True

# print(isAllDigits("12345"))
# print(isAllDigits("123a5"))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Count the number of words in a string.
# Input:  "  hello world  "  →  Output: 2

def countWords(s:str):
    return len(s.split())

# print(countWords("hello    world"))

# ==========================================Revision needed =============================================
# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Check if a string is a subsequence of another.
# Input:  s="abc", t="ahbgdc"  →  Output: True
# Input:  s="axc", t="ahbgdc"  →  Output: False

def isSubsequence(s, t):
    i=0
    j=0
    while j < len(t):
        if i < len(s) and s[i]==t[j]:
                i+=1
                if i == len(s):
                    return True
        j+=1
    return False

        

# print(isSubsequence("abc", "ahbgdc"))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Caesar cipher — shift each letter by k positions.
# Input:  "hello", k=3  →  Output: "khoor"

def caesarCipher(s, k):
    newstr = ""

    for ch in s:
        position = ord(ch) - ord('a')   # Convert 'a'-'z' to 0-25
        shifted = (position + k) % 26   # Shift and wrap around
        newstr += chr(shifted + ord('a'))  # Convert back to character

    return newstr

# print(caesarCipher("hello", 3))   # khoor
# print(caesarCipher("xyz", 3))     # abc


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Valid parentheses — check if brackets are properly opened and closed.
# Input:  "()[]{}"   →  Output: True
# Input:  "(]"       →  Output: False
# Input:  "([)]"     →  Output: False

def isValidParentheses(s):
    isvalid={
        "(":")",
        "[":"]",
        "{":"}"
    }
    stack:list[str]=[]
    for ch in s:
        if ch in isvalid:
            stack.append(ch)
        else :
            if len(stack) == 0:
                return False
            top = stack[-1]
            if isvalid[top] == ch:
                stack.pop()
            else:
                return False
    return len(stack)==0


# print(isValidParentheses("()[]{}"))
# print(isValidParentheses("{[()]}"))


# [E-17] -----------------------------------------------------------------------------------------------------------------------
# Compress a string using counts of repeated characters.
# Input:  "aabcccccaaa"  →  Output: "a2b1c5a3"
# Rule: if compressed is not shorter, return original.

def compressString(s):
    pass

# print(compressString("aabcccccaaa"))


# [E-18] -----------------------------------------------------------------------------------------------------------------------
# Ransom note — can you build t using letters from s (each letter used once)?
# Input:  s="aab", t="a"   →  Output: True
# Input:  s="aab", t="aab" →  Output: True
# Input:  s="aab", t="aaab"→  Output: False

def canConstruct(s, t):
    pass

# print(canConstruct("aab", "a"))


# =============================================================================================================================
# MEDIUM (38 problems) — Sliding Window | Two Pointers | Hashing | Stack | DP
# =============================================================================================================================

# ----- SLIDING WINDOW (12 problems) ------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Longest substring without repeating characters.
# Input:  "abcabcbb"  →  Output: 3  ("abc")
# Input:  "bbbbb"     →  Output: 1  ("b")
# Input:  "pwwkew"    →  Output: 3  ("wke")

def lengthOfLongestSubstring(s):
    pass

print(lengthOfLongestSubstring("abcabcbb"))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Longest substring with at most k distinct characters.
# Input:  "eceba", k=2  →  Output: 3  ("ece")
# Input:  "aa", k=1     →  Output: 2

def longestSubstringKDistinct(s, k):
    pass

# print(longestSubstringKDistinct("eceba", 2))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Permutation in string — check if any permutation of s1 exists as substring in s2.
# Input:  s1="ab", s2="eidbaooo"   →  Output: True  ("ba" at index 3)
# Input:  s1="ab", s2="eidboaoo"   →  Output: False

def checkInclusion(s1, s2):
    pass

# print(checkInclusion("ab", "eidbaooo"))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Find all anagrams in a string — return start indices of all anagrams of p in s.
# Input:  s="cbaebabacd", p="abc"  →  Output: [0, 6]

def findAnagrams(s, p):
    pass

# print(findAnagrams("cbaebabacd", "abc"))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Longest repeating character replacement — replace at most k chars to get longest same-char window.
# Input:  "AABABBA", k=1  →  Output: 4
# Input:  "ABAB", k=2     →  Output: 4

def characterReplacement(s, k):
    pass

# print(characterReplacement("AABABBA", 1))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Max consecutive ones III — flip at most k zeros to get longest run of 1s.
# Input:  [1,1,1,0,0,0,1,1,1,1,0], k=2  →  Output: 6

def longestOnes(arr, k):
    pass

# print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Number of substrings containing all three characters a, b, c at least once.
# Input:  "abcabc"  →  Output: 10

def numberOfSubstrings(s):
    pass

# print(numberOfSubstrings("abcabc"))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Longest substring with at most 2 distinct characters.
# Input:  "eceba"   →  Output: 3  ("ece")
# Input:  "ccaabbb" →  Output: 5  ("aabbb")

def lengthOfLongestSubstringTwoDistinct(s):
    pass

# print(lengthOfLongestSubstringTwoDistinct("eceba"))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Minimum window substring — smallest window in s containing all chars of t.
# Input:  s="ADOBECODEBANC", t="ABC"  →  Output: "BANC"
# Input:  s="a", t="a"                →  Output: "a"

def minWindow(s, t):
    pass

# print(minWindow("ADOBECODEBANC", "ABC"))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Fruit into baskets (string version) — longest subarray with at most 2 distinct chars.
# Input:  "AAABBB"  →  Output: 6
# Input:  "AABACB"  →  Output: 4  ("AABA" or "ACBA")

def fruitsInBaskets(s):
    pass

# print(fruitsInBaskets("AABACB"))


# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Subarrays with k different integers (string equivalent — substrings with exactly k distinct).
# Input:  "araaci", k=2  →  Output: 7

def subarraysWithKDistinct(s, k):
    pass

# print(subarraysWithKDistinct("araaci", 2))


# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Longest beautiful substring — substring where each letter appears at least k times
# and has exactly numUniqueLetters unique letters.
# Input:  "aabbcc", k=2  →  Output: 6

def longestBeautifulSubstring(s, k):
    pass

# print(longestBeautifulSubstring("aabbcc", 2))


# ----- TWO POINTERS (6 problems) ---------------------------------------------------------------------------------------------

# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Valid palindrome II — can you remove at most one character to make it a palindrome?
# Input:  "abca"  →  Output: True  (remove 'b' or 'c')
# Input:  "abc"   →  Output: False

def validPalindromeII(s):
    pass

# print(validPalindromeII("abca"))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Reverse vowels of a string.
# Input:  "hello"   →  Output: "holle"
# Input:  "leetcode" →  Output: "leotcede"

def reverseVowels(s):
    pass

# print(reverseVowels("hello"))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Reverse only letters — keep non-letter characters in place.
# Input:  "a-bC-dEf-ghIj"  →  Output: "j-Ih-gfE-dCba"

def reverseOnlyLetters(s):
    pass

# print(reverseOnlyLetters("a-bC-dEf-ghIj"))


# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Backspace string compare — '#' deletes the previous character. Are the two strings equal?
# Input:  s="ab#c", t="ad#c"   →  Output: True  (both become "ac")
# Input:  s="ab##", t="c#d#"   →  Output: True  (both become "")

def backspaceCompare(s, t):
    pass

# print(backspaceCompare("ab#c", "ad#c"))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Longest palindromic substring (expand around center).
# Input:  "babad"  →  Output: "bab"  (or "aba")
# Input:  "cbbd"   →  Output: "bb"

def longestPalindrome(s):
    pass

# print(longestPalindrome("babad"))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Count palindromic substrings.
# Input:  "abc"   →  Output: 3   (a, b, c)
# Input:  "aaa"   →  Output: 6   (a, a, a, aa, aa, aaa)

def countPalindromes(s):
    pass

# print(countPalindromes("aaa"))


# ----- HASHING (10 problems) -------------------------------------------------------------------------------------------------

# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Group anagrams — group strings that are anagrams of each other.
# Input:  ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

def groupAnagrams(strs):
    pass

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Isomorphic strings — can you map each char in s to a char in t consistently?
# Input:  s="egg", t="add"   →  Output: True
# Input:  s="foo", t="bar"   →  Output: False

def isIsomorphic(s, t):
    pass

# print(isIsomorphic("egg", "add"))


# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Word pattern — does s follow the same pattern as a string of words?
# Input:  pattern="abba", s="dog cat cat dog"  →  Output: True
# Input:  pattern="abba", s="dog cat cat fish" →  Output: False

def wordPattern(pattern, s):
    pass

# print(wordPattern("abba", "dog cat cat dog"))


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Subdomain visit count — count visits for each subdomain level.
# Input:  ["9001 discuss.leetcode.com"]
# Output: ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

def subdomainVisits(cpdomains):
    pass

# print(subdomainVisits(["9001 discuss.leetcode.com"]))


# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Find all duplicate words in a sentence.
# Input:  "the sky is blue sky and the"  →  Output: ["sky", "the"]

def findDuplicateWords(sentence):
    pass

# print(findDuplicateWords("the sky is blue sky and the"))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Top k frequent words.
# Input:  ["i","love","leetcode","i","love","coding"], k=2  →  Output: ["i","love"]

def topKFrequentWords(words, k):
    pass

# print(topKFrequentWords(["i","love","leetcode","i","love","coding"], 2))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Custom sort string — sort t using the order defined in order string.
# Input:  order="cba", t="abcd"  →  Output: "cbad"

def customSortString(order, t):
    pass

# print(customSortString("cba", "abcd"))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Buddy strings — can you swap exactly one pair in s to make it equal to goal?
# Input:  s="ab", goal="ba"   →  Output: True
# Input:  s="ab", goal="ab"   →  Output: False

def buddyStrings(s, goal):
    pass

# print(buddyStrings("ab", "ba"))


# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Unique email addresses — count distinct addresses after processing '+' and '.' rules.
# Input:  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com"]
# Output: 2

def numUniqueEmails(emails):
    pass

# print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com"]))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# String to integer — count ways to decode a digit string (1→A, 2→B, ..., 26→Z).
# Input:  "12"   →  Output: 2  ("AB" or "L")
# Input:  "226"  →  Output: 3  ("BZ","VF","BBF")

def numDecodings(s):
    pass

# print(numDecodings("226"))


# ----- STACK-BASED (6 problems) ----------------------------------------------------------------------------------------------

# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Decode string — decode "k[encoded_string]" patterns.
# Input:  "3[a]2[bc]"    →  Output: "aaabcbc"
# Input:  "3[a2[c]]"     →  Output: "accaccacc"

def decodeString(s):
    pass

# print(decodeString("3[a]2[bc]"))


# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Remove all adjacent duplicates in a string (one pass).
# Input:  "abbaca"   →  Output: "ca"

def removeDuplicatesStack(s):
    pass

# print(removeDuplicatesStack("abbaca"))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Remove k digits to make the smallest number possible.
# Input:  "1432219", k=3  →  Output: "1219"
# Input:  "10200", k=1    →  Output: "200"

def removeKdigits(num, k):
    pass

# print(removeKdigits("1432219", 3))


# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Simplify path — simplify a Unix file path.
# Input:  "/home/"          →  Output: "/home"
# Input:  "/../"            →  Output: "/"
# Input:  "/home//foo/"     →  Output: "/home/foo"

def simplifyPath(path):
    pass

# print(simplifyPath("/home//foo/"))


# [M-33] -----------------------------------------------------------------------------------------------------------------------
# Score of parentheses — compute score where "()" = 1, AB = A+B, (A) = 2*A.
# Input:  "()"      →  Output: 1
# Input:  "(())"    →  Output: 2
# Input:  "()()"    →  Output: 2

def scoreOfParentheses(s):
    pass

# print(scoreOfParentheses("(()(()))"))


# [M-34] -----------------------------------------------------------------------------------------------------------------------
# Longest valid parentheses — length of longest valid bracket substring.
# Input:  "(()"    →  Output: 2
# Input:  ")()())" →  Output: 4

def longestValidParentheses(s):
    pass

# print(longestValidParentheses(")()())"))


# ----- MIXED MEDIUM (4 problems) ---------------------------------------------------------------------------------------------

# [M-35] -----------------------------------------------------------------------------------------------------------------------
# ZigZag conversion — write string in zigzag pattern across numRows rows.
# Input:  "PAYPALISHIRING", numRows=3  →  Output: "PAHNAPLSIIGYIR"

def zigzagConversion(s, numRows):
    pass

# print(zigzagConversion("PAYPALISHIRING", 3))


# [M-36] -----------------------------------------------------------------------------------------------------------------------
# Compare version numbers — compare "1.01" vs "1.001" (leading zeros ignored).
# Input:  "1.01", "1.001"  →  Output: 0  (equal)
# Input:  "1.0", "1.0.0"   →  Output: 0
# Input:  "0.1", "1.1"     →  Output: -1

def compareVersion(v1, v2):
    pass

# print(compareVersion("1.01", "1.001"))


# [M-37] -----------------------------------------------------------------------------------------------------------------------
# Largest number — arrange numbers to form the largest number.
# Input:  [3, 30, 34, 5, 9]  →  Output: "9534330"

def largestNumber(nums):
    pass

# print(largestNumber([3, 30, 34, 5, 9]))


# [M-38] -----------------------------------------------------------------------------------------------------------------------
# Count and say — generate nth term of the count-and-say sequence.
# Input:  n=4  →  Output: "1211"  (1 → "11" → "21" → "1211")

def countAndSay(n):
    pass

# print(countAndSay(4))


# =============================================================================================================================
# HARD (12 problems) — Stretch your thinking, pick selectively
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Minimum window substring (hard constraints — follow-up: what if t has duplicates?).
# Already in medium M-09, revisit here with optimal O(n) solution and edge cases.
# Input:  s="ADOBECODEBANC", t="AABC"  →  Output: "ADOBEC"

def minWindowHard(s, t):
    pass

# print(minWindowHard("ADOBECODEBANC", "AABC"))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Regular expression matching — '.' matches any char, '*' matches zero or more of preceding.
# Input:  s="aa", p="a*"   →  Output: True
# Input:  s="ab", p=".*"   →  Output: True

def isMatchRegex(s, p):
    pass

# print(isMatchRegex("aa", "a*"))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Wildcard matching — '?' matches single char, '*' matches any sequence.
# Input:  s="adceb", p="*a*b"  →  Output: True
# Input:  s="acdcb", p="a*c?b" →  Output: False

def isMatchWildcard(s, p):
    pass

# print(isMatchWildcard("adceb", "*a*b"))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Edit distance (Levenshtein) — minimum operations to convert word1 to word2.
# Input:  "horse", "ros"  →  Output: 3

def minDistance(word1, word2):
    pass

# print(minDistance("horse", "ros"))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Interleaving string — check if s3 is formed by interleaving s1 and s2.
# Input:  s1="aabcc", s2="dbbca", s3="aadbbcbcac"  →  Output: True

def isInterleave(s1, s2, s3):
    pass

# print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# Distinct subsequences — count distinct ways to form t as subsequence of s.
# Input:  s="rabbbit", t="rabbit"  →  Output: 3

def numDistinct(s, t):
    pass

# print(numDistinct("rabbbit", "rabbit"))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Palindrome partitioning II — minimum cuts to partition string into all palindromes.
# Input:  "aab"   →  Output: 1  (["aa","b"])
# Input:  "aabb"  →  Output: 1  (["aa","bb"])

def minCutPalindrome(s):
    pass

# print(minCutPalindrome("aab"))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Shortest palindrome — add minimum characters in front to make it a palindrome.
# Input:  "aacecaaa"  →  Output: "aaacecaaa"
# Input:  "abcd"      →  Output: "dcbabcd"

def shortestPalindrome(s):
    pass

# print(shortestPalindrome("abcd"))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# Longest palindromic substring using Manacher's algorithm (O(n)).
# Input:  "babad"  →  Output: "bab"

def longestPalindromeManacher(s):
    pass

# print(longestPalindromeManacher("babad"))


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Word break — can string be segmented into words from a dictionary?
# Input:  s="leetcode", wordDict=["leet","code"]  →  Output: True
# Input:  s="applepenapple", wordDict=["apple","pen"]  →  Output: True

def wordBreak(s, wordDict):
    pass

# print(wordBreak("leetcode", ["leet","code"]))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Word break II — return all possible sentence splits.
# Input:  s="catsanddog", wordDict=["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

def wordBreakII(s, wordDict):
    pass

# print(wordBreakII("catsanddog", ["cat","cats","and","sand","dog"]))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Concatenated words — find all words in array that are formed by concatenating other words.
# Input:  ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

def findAllConcatenatedWords(words):
    pass

# print(findAllConcatenatedWords(["cat","cats","catsdogcats","dog","dogcatsdog","rat","ratcatdogcat"]))
