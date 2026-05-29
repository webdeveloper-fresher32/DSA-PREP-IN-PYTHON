# =============================================================================================================================
# RECURSION — PROBLEM SET  (~14 problems)
# Progress: Easy [0/4] | Medium [0/6] | Hard [0/4]
#
# Daily target: 1 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
#
# RECURSION TEMPLATE:
#   def solve(problem):
#       if base_case(problem):       ← smallest possible input
#           return base_answer
#       smaller = reduce(problem)    ← make problem smaller
#       sub = solve(smaller)         ← trust this works
#       return combine(sub)          ← build the full answer
#
# Patterns: Basic | Math | List Recursion | Backtracking | Divide & Conquer
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Base cases, simple recursive calls
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Return n! recursively. Base case: 0! = 1.
# Input:  5  →  Output: 120
# Input:  0  →  Output: 1

def factorial(n):
    pass

# print(factorial(5))
# print(factorial(0))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Recursively sum all elements in a list.
# Input:  [1,2,3,4,5]  →  Output: 15

def sumList(nums):
    pass

# print(sumList([1,2,3,4,5]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Reverse a string using recursion (no slicing or built-ins).
# Input:  "hello"  →  Output: "olleh"

def reverseString(s):
    pass

# print(reverseString("hello"))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Return a list counting down from n to 0 recursively.
# Input:  5  →  Output: [5, 4, 3, 2, 1, 0]

def countdown(n):
    pass

# print(countdown(5))


# =============================================================================================================================
# MEDIUM (6 problems) — Multi-branch recursion | Memoization | Structural recursion
# =============================================================================================================================

# ----- MATH RECURSION (3 problems) -------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Return the nth Fibonacci number recursively.
# fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
# Input:  10  →  Output: 55

def fibonacci(n):
    pass

# print(fibonacci(10))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Compute base^exp recursively using fast exponentiation:
# base^0 = 1, base^even = (base^(exp//2))^2, base^odd = base * base^(exp-1)
# Input:  2, 10  →  Output: 1024

def power(base, exp):
    pass

# print(power(2, 10))
# print(power(3, 0))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Tower of Hanoi — print the moves to solve for n disks and return total move count.
# Format: "Move disk X from A to C"
# Input:  n=3  →  Output: 7  (printed + returned)

def hanoi(n, source="A", target="C", aux="B"):
    pass

# print(hanoi(3))


# ----- LIST / STRUCTURE RECURSION (3 problems) -------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Recursively flatten a list nested to any depth.
# Input:  [1,[2,[3,[4]],5]]  →  Output: [1,2,3,4,5]

def flatten(nested):
    pass

# print(flatten([1,[2,[3,[4]],5]]))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Binary search recursively — return index of target or -1.
# Input:  [1,3,5,7,9,11], target=7  →  Output: 3
# Input:  [1,3,5,7,9,11], target=4  →  Output: -1

def binarySearch(nums, target, low=None, high=None):
    pass

# print(binarySearch([1,3,5,7,9,11], 7))
# print(binarySearch([1,3,5,7,9,11], 4))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Given a sorted array, count how many times it has been rotated (find index of minimum).
# Input:  [4,5,6,7,0,1,2]  →  Output: 4   (rotated 4 times, minimum is at index 4)
# Input:  [1,2,3,4,5]      →  Output: 0   (not rotated)

def findRotationCount(nums, low=None, high=None):
    pass

# print(findRotationCount([4,5,6,7,0,1,2]))
# print(findRotationCount([1,2,3,4,5]))


# =============================================================================================================================
# HARD (4 problems) — Backtracking | Divide & Conquer
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Return all possible subsets (power set) of a list of unique integers.
# Input:  [1,2,3]  →  Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

def allSubsets(nums):
    pass

# print(allSubsets([1,2,3]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Return all permutations of a list of unique integers.
# Input:  [1,2,3]  →  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permutations(nums):
    pass

# print(permutations([1,2,3]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Return all combinations of n pairs of balanced parentheses.
# Input:  2  →  Output: ["(())", "()()"]
# Input:  3  →  Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

def generateParentheses(n):
    pass

# print(generateParentheses(2))
# print(generateParentheses(3))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Merge sort — sort a list using the divide-and-conquer recursive approach.
# Input:  [38,27,43,3,9,82,10]  →  Output: [3,9,10,27,38,43,82]

def mergeSort(nums):
    pass

# print(mergeSort([38,27,43,3,9,82,10]))
