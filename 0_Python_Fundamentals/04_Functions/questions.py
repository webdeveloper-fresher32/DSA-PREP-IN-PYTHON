# =============================================================================================================================
# FUNCTIONS — PROBLEM SET  (~13 problems)
# Progress: Easy [0/4] | Medium [0/6] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Patterns: Basic Functions | Default Args | *args/**kwargs | Higher-Order | Decomposition
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Return values, basic decomposition
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Return a tuple (min_val, max_val) from a list of integers WITHOUT using min() or max().
# Input:  [3, 1, 4, 1, 5, 9, 2]  →  Output: (1, 9)

def minMax(nums):
    pass

# print(minMax([3, 1, 4, 1, 5, 9, 2]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Compute base^exponent using a loop (not ** or pow()).
# Input:  2, 10  →  Output: 1024
# Input:  3, 0   →  Output: 1

def power(base, exponent):
    pass

# print(power(2, 10))
# print(power(3, 0))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Return True if a string reads the same forwards and backwards. Ignore case.
# Input:  "Racecar"  →  Output: True
# Input:  "hello"    →  Output: False

def isPalindrome(s):
    pass

# print(isPalindrome("Racecar"))
# print(isPalindrome("hello"))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Decompose into two functions:
# getFactors(n)  → return all proper factors of n (excluding n itself)
# isPerfect(n)   → return True if n equals the sum of its proper factors
# 28 is perfect: factors are [1,2,4,7,14], sum = 28
# Input:  28  →  getFactors: [1,2,4,7,14]  |  isPerfect: True
# Input:  12  →  isPerfect: False

def getFactors(n):
    pass

def isPerfect(n):
    pass

# print(getFactors(28))
# print(isPerfect(28))
# print(isPerfect(12))


# =============================================================================================================================
# MEDIUM (6 problems) — Default args | *args | Higher-order functions
# =============================================================================================================================

# ----- DEFAULT ARGS & *ARGS (3 problems) -------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# greet(name, greeting="Hello") returns "{greeting}, {name}!"
# Then write makeGreeter(greeting) that RETURNS a pre-configured greeter function.
# greet("Alice")         →  "Hello, Alice!"
# greet("Alice", "Hi")   →  "Hi, Alice!"
# hi = makeGreeter("Hi")
# hi("Bob")              →  "Hi, Bob!"

def greet(name, greeting="Hello"):
    pass

def makeGreeter(greeting):
    pass

# print(greet("Alice"))
# print(greet("Alice", "Hi"))
# hi = makeGreeter("Hi")
# print(hi("Bob"))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Use *args: given any number of integers, return their running totals as a list.
# Input:  1, 2, 3, 4  →  Output: [1, 3, 6, 10]

def runningTotal(*nums):
    pass

# print(runningTotal(1, 2, 3, 4))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Use **kwargs: given keyword arguments representing a person's attributes,
# return a formatted string "Name: X, Age: Y, City: Z" (only include keys that exist).
# Input:  name="Alice", age=30, city="Sydney"  →  "Name: Alice, Age: 30, City: Sydney"
# Input:  name="Bob", age=25                   →  "Name: Bob, Age: 25"

def formatPerson(**kwargs):
    pass

# print(formatPerson(name="Alice", age=30, city="Sydney"))
# print(formatPerson(name="Bob", age=25))


# ----- HIGHER-ORDER FUNCTIONS (3 problems) -----------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# applyTwice(func, value) applies func to value, then applies func to the result.
# Input:  lambda x: x + 3,  7  →  Output: 13   (7+3=10, 10+3=13)
# Input:  lambda x: x * 2,  4  →  Output: 16   (4*2=8, 8*2=16)

def applyTwice(func, value):
    pass

# print(applyTwice(lambda x: x + 3, 7))
# print(applyTwice(lambda x: x * 2, 4))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# pipeline(value, *functions) passes value through each function in order.
# Input:  5, lambda x: x*2, lambda x: x+1, str  →  Output: "11"

def pipeline(value, *functions):
    pass

# print(pipeline(5, lambda x: x*2, lambda x: x+1, str))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# myMap(func, lst) applies func to every element of lst and returns the result list.
# myFilter(func, lst) returns only elements where func returns True.
# Do NOT use the built-in map() or filter().
# myMap(lambda x: x**2, [1,2,3,4])        →  [1, 4, 9, 16]
# myFilter(lambda x: x % 2 == 0, [1,2,3,4,5,6])  →  [2, 4, 6]

def myMap(func, lst):
    pass

def myFilter(func, lst):
    pass

# print(myMap(lambda x: x**2, [1,2,3,4]))
# print(myFilter(lambda x: x % 2 == 0, [1,2,3,4,5,6]))


# =============================================================================================================================
# HARD (3 problems) — Closures, memoization, function composition
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Write makeCounter() that returns a counter function. Each time the counter
# is called, it increments and returns the new count. Each counter is independent.
# c1 = makeCounter()
# c1()  →  1
# c1()  →  2
# c2 = makeCounter()
# c2()  →  1   (independent of c1)

def makeCounter():
    pass

# c1 = makeCounter()
# print(c1())   # 1
# print(c1())   # 2
# c2 = makeCounter()
# print(c2())   # 1


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Memoized fibonacci using a dictionary cache inside the function.
# fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)
# Must compute fib(50) quickly (under 1 second).
# Input:  10  →  Output: 55
# Input:  50  →  Output: 12586269025

def fibMemo(n, memo={}):
    pass

# print(fibMemo(10))
# print(fibMemo(50))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Write memoize(func) — a decorator-style function that wraps any function
# and caches its results so repeated calls with same arguments are instant.
# Then use it to wrap a slow squaring function and verify caching works.

def memoize(func):
    pass

# def slowSquare(n):
#     return n * n
#
# fastSquare = memoize(slowSquare)
# print(fastSquare(5))   # 25
# print(fastSquare(5))   # 25 (from cache)
# print(fastSquare(10))  # 100
