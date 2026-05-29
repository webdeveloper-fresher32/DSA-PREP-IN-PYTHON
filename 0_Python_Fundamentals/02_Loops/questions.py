# =============================================================================================================================
# LOOPS — PROBLEM SET  (~14 problems)
# Progress: Easy [0/5] | Medium [0/6] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Patterns: Basic Iteration | Nested Loops | While Loops | Loop + Math
# =============================================================================================================================


# =============================================================================================================================
# EASY (5 problems) — Single loops, simple counters
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Return the sum of all integers from 1 to n (inclusive).
# Input:  5   →  Output: 15   (1+2+3+4+5)
# Input:  10  →  Output: 55

def sumToN(n):
    pass

# print(sumToN(5))
# print(sumToN(10))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Return a list of strings for numbers 1 to n using FizzBuzz rules:
# divisible by 3 → "Fizz", by 5 → "Buzz", by both → "FizzBuzz", else the number as string.
# Input:  5  →  Output: ["1", "2", "Fizz", "4", "Buzz"]

def fizzBuzz(n):
    pass

# print(fizzBuzz(15))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Given a list of integers, return how many are even.
# Input:  [1, 2, 3, 4, 5, 6]  →  Output: 3

def countEvens(nums):
    pass

# print(countEvens([1, 2, 3, 4, 5, 6]))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Return the factorial of n using a loop (not recursion). 0! = 1.
# Input:  5  →  Output: 120
# Input:  0  →  Output: 1

def factorial(n):
    pass

# print(factorial(5))
# print(factorial(0))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Repeatedly sum the digits of n until you get a single digit. Return it.
# Input:  493   →  4+9+3=16 → 1+6=7  →  Output: 7
# Input:  9999  →  36 → 9            →  Output: 9

def digitRoot(n):
    pass

# print(digitRoot(493))
# print(digitRoot(9999))


# =============================================================================================================================
# MEDIUM (6 problems) — Nested Loops | While Logic | Pattern Building
# =============================================================================================================================

# ----- NESTED LOOPS (3 problems) ---------------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Given a list of pairs [[a,b], [c,d], ...], return a list of their sums.
# Input:  [[1,2],[3,4],[5,6]]  →  Output: [3, 7, 11]

def pairSums(pairs):
    pass

# print(pairSums([[1,2],[3,4],[5,6]]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Return an n x n multiplication table as a 2D list.
# n=3  →  [[1,2,3],[2,4,6],[3,6,9]]

def multiplicationTable(n):
    pass

# print(multiplicationTable(3))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Given n, return a spiral matrix of numbers 1 to n*n as a 2D list (clockwise spiral).
# n=3  →  [[1,2,3],[8,9,4],[7,6,5]]

def spiralMatrix(n):
    pass

# print(spiralMatrix(3))


# ----- WHILE LOOPS (3 problems) ----------------------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Return the first prime number greater than n.
# Input:  10  →  Output: 11
# Input:  13  →  Output: 17

def nextPrime(n):
    pass

# print(nextPrime(10))
# print(nextPrime(13))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Each step: if n is even → divide by 2, if odd → subtract 1.
# Return the number of steps to reach 0.
# Input:  14  →  Output: 6   (14→7→6→3→2→1→0)
# Input:  8   →  Output: 4   (8→4→2→1→0)

def stepsToZero(n):
    pass

# print(stepsToZero(14))
# print(stepsToZero(8))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Collatz conjecture: if n is even divide by 2, if odd multiply by 3 and add 1.
# Return the number of steps to reach 1.
# Input:  6   →  Output: 8   (6→3→10→5→16→8→4→2→1)
# Input:  27  →  Output: 111

def collatzSteps(n):
    pass

# print(collatzSteps(6))
# print(collatzSteps(27))


# =============================================================================================================================
# HARD (3 problems) — Complex iteration, simulation
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Return a list of all prime numbers up to and including n (Sieve of Eratosthenes).
# Input:  20  →  Output: [2, 3, 5, 7, 11, 13, 17, 19]

def sieveOfEratosthenes(n):
    pass

# print(sieveOfEratosthenes(20))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Given a number n, return all pairs (a, b) where a <= b and a^2 + b^2 == n.
# Input:  50  →  Output: [(1, 7), (5, 5)]
# Input:  25  →  Output: [(0, 5), (3, 4)]

def pythagoreanPairs(n):
    pass

# print(pythagoreanPairs(50))
# print(pythagoreanPairs(25))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Print Pascal's triangle up to n rows. Return it as a list of lists.
# n=5  →  [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def pascalTriangle(n):
    pass

# print(pascalTriangle(5))
