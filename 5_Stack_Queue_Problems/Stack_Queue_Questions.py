# =============================================================================================================================
# STACKS & QUEUES — COMPLETE PROBLEM SET  (~65 problems)
# Progress: Easy [0/17] | Medium [0/36] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Patterns: Monotonic Stack | Bracket Matching | Expression Eval | Deque/Sliding Window | BFS Queue
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (17 problems) — Build comfort with stack/queue mechanics
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Implement a stack using a list. Support push, pop, top, isEmpty.
# push(1), push(2), top() → 2, pop() → 2, isEmpty() → False

class MyStack:
    def __init__(self):
        pass
    def push(self, val):
        pass
    def pop(self):
        pass
    def top(self):
        pass
    def isEmpty(self):
        pass

# s = MyStack(); s.push(1); s.push(2); print(s.top())


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Implement a queue using a list. Support enqueue, dequeue, front, isEmpty.
# enqueue(1), enqueue(2), front() → 1, dequeue() → 1, front() → 2

class MyQueue:
    def __init__(self):
        pass
    def enqueue(self, val):
        pass
    def dequeue(self):
        pass
    def front(self):
        pass
    def isEmpty(self):
        pass

# q = MyQueue(); q.enqueue(1); q.enqueue(2); print(q.front())


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Valid parentheses — check if brackets are properly opened and closed.
# Input:  "()[]{}"   →  Output: True
# Input:  "([)]"     →  Output: False
# Input:  "{[]}"     →  Output: True

def isValidParentheses(s):
    pass

# print(isValidParentheses("()[]{}"))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Min stack — stack that supports push, pop, top, and getMin in O(1).
# push(-2), push(0), push(-3), getMin() → -3, pop(), top() → 0, getMin() → -2

class MinStack:
    def __init__(self):
        pass
    def push(self, val):
        pass
    def pop(self):
        pass
    def top(self):
        pass
    def getMin(self):
        pass

# ms = MinStack(); ms.push(-2); ms.push(0); ms.push(-3); print(ms.getMin())


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Reverse a string using a stack.
# Input:  "hello"  →  Output: "olleh"

def reverseWithStack(s):
    pass

# print(reverseWithStack("hello"))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Baseball game — evaluate a list of operations on scores.
# "+": sum of last two, "D": double last, "C": remove last, number: add it.
# Input:  ["5","2","C","D","+"]  →  Output: 30

def calPoints(ops):
    pass

# print(calPoints(["5","2","C","D","+"]))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Remove all adjacent duplicates in a string (one-pass using stack).
# Input:  "abbaca"   →  Output: "ca"
# Input:  "azxxzy"   →  Output: "ay"

def removeDuplicates(s):
    pass

# print(removeDuplicates("abbaca"))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Implement queue using two stacks. Support push, pop, peek, empty.
# push(1), push(2), peek() → 1, pop() → 1, empty() → False

class QueueUsingStacks:
    def __init__(self):
        pass
    def push(self, x):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def empty(self):
        pass

# q = QueueUsingStacks(); q.push(1); q.push(2); print(q.peek())


# [E-09] -----------------------------------------------------------------------------------------------------------------------
# Implement stack using two queues. Support push, pop, top, empty.
# push(1), push(2), top() → 2, pop() → 2

class StackUsingQueues:
    def __init__(self):
        pass
    def push(self, x):
        pass
    def pop(self):
        pass
    def top(self):
        pass
    def empty(self):
        pass

# s = StackUsingQueues(); s.push(1); s.push(2); print(s.top())


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Next greater element I — for each element in nums1, find next greater in nums2.
# Input:  nums1=[4,1,2], nums2=[1,3,4,2]  →  Output: [-1,3,-1]

def nextGreaterElementI(nums1, nums2):
    pass

# print(nextGreaterElementI([4,1,2], [1,3,4,2]))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Number of students unable to eat lunch — students leave if top sandwich matches preference.
# Input:  students=[1,1,0,0], sandwiches=[0,1,0,1]  →  Output: 0

def countStudents(students, sandwiches):
    pass

# print(countStudents([1,1,0,0], [0,1,0,1]))


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Time needed to buy tickets — person at index k buys 1 ticket per round until their count is 0.
# Input:  tickets=[2,3,2], k=2  →  Output: 6

def timeRequiredToBuy(tickets, k):
    pass

# print(timeRequiredToBuy([2,3,2], 2))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Reverse first k elements of a queue.
# Input:  queue=[1,2,3,4,5], k=3  →  Output: [3,2,1,4,5]

def reverseFirstK(queue, k):
    pass

# print(reverseFirstK([1,2,3,4,5], 3))


# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Check if array is stack-sortable — can it be sorted using one auxiliary stack?
# Input:  [3,2,1]  →  Output: True
# Input:  [3,1,2]  →  Output: False

def isStackSortable(arr):
    pass

# print(isStackSortable([3,2,1]))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Evaluate a simple postfix (Reverse Polish Notation) expression.
# Input:  ["2","1","+","3","*"]  →  Output: 9   ((2+1)*3)
# Input:  ["4","13","5","/","+"]  →  Output: 6  (4+(13/5))

def evalRPN(tokens):
    pass

# print(evalRPN(["2","1","+","3","*"]))


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Moving average from a data stream — average of last k values.
# Input:  k=3, stream=[1,10,3,5]  →  Output: [1.0, 5.5, 4.67, 6.0]

class MovingAverage:
    def __init__(self, size):
        pass
    def next(self, val):
        pass

# ma = MovingAverage(3); print([ma.next(x) for x in [1,10,3,5]])


# [E-17] -----------------------------------------------------------------------------------------------------------------------
# First unique character in a stream — after each character, return first non-repeating char or '#'.
# Input:  "aabccxb"  →  Output: "a#b##x#"  (after each char)

def firstNonRepeatingStream(s):
    pass

# print(firstNonRepeatingStream("aabccxb"))


# =============================================================================================================================
# MEDIUM (36 problems) — Monotonic Stack | Expressions | Deque | BFS Queue
# =============================================================================================================================

# ----- MONOTONIC STACK (12 problems) -----------------------------------------------------------------------------------------
# Core idea: maintain a stack that is always increasing or decreasing.
# Use to find: next greater/smaller, previous greater/smaller, span, histogram areas.

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Daily temperatures — for each day, how many days until a warmer temperature?
# Input:  [73,74,75,71,69,72,76,73]  →  Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temps):
    pass

# print(dailyTemperatures([73,74,75,71,69,72,76,73]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Next greater element II — circular array, find next greater for each element.
# Input:  [1,2,1]  →  Output: [2,-1,2]

def nextGreaterElementII(nums):
    pass

# print(nextGreaterElementII([1,2,1]))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Online stock span — span = number of consecutive days price was <= today's price.
# Input:  prices=[100,80,60,70,60,75,85]  →  Output: [1,1,1,2,1,4,6]

class StockSpanner:
    def __init__(self):
        pass
    def next(self, price):
        pass

# sp = StockSpanner(); print([sp.next(p) for p in [100,80,60,70,60,75,85]])


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Sum of subarray minimums — sum of min of every subarray.
# Input:  [3,1,2,4]  →  Output: 17

def sumSubarrayMins(arr):
    pass

# print(sumSubarrayMins([3,1,2,4]))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Remove k digits to form the smallest number (monotonic stack on string).
# Input:  "1432219", k=3  →  Output: "1219"
# Input:  "10200", k=1    →  Output: "200"

def removeKdigits(num, k):
    pass

# print(removeKdigits("1432219", 3))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Asteroid collision — positive moves right, negative moves left. Find final state.
# Input:  [5,10,-5]   →  Output: [5,10]  (-5 destroyed by 10)
# Input:  [8,-8]      →  Output: []      (both destroyed)
# Input:  [10,2,-5]   →  Output: [10]

def asteroidCollision(asteroids):
    pass

# print(asteroidCollision([5,10,-5]))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# 132 pattern — find i < j < k such that arr[i] < arr[k] < arr[j].
# Input:  [3,1,4,2]  →  Output: True  (1 < 2 < 4)
# Input:  [-1,3,2,0] →  Output: True

def find132pattern(nums):
    pass

# print(find132pattern([3,1,4,2]))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Previous smaller element — for each element, find the nearest smaller on the left.
# Input:  [4,5,2,10,8]  →  Output: [-1,4,-1,2,2]

def previousSmallerElement(arr):
    pass

# print(previousSmallerElement([4,5,2,10,8]))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Next smaller element — for each element, find the nearest smaller on the right.
# Input:  [4,5,2,10,8]  →  Output: [2,2,-1,8,-1]

def nextSmallerElement(arr):
    pass

# print(nextSmallerElement([4,5,2,10,8]))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Largest rectangle in histogram.
# Input:  [2,1,5,6,2,3]  →  Output: 10

def largestRectangle(heights):
    pass

# print(largestRectangle([2,1,5,6,2,3]))


# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Trapping rain water (monotonic stack approach).
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]  →  Output: 6

def trapWater(height):
    pass

# print(trapWater([0,1,0,2,1,0,1,3,2,1,2,1]))


# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Maximum width ramp — find max j-i where j>i and arr[j]>=arr[i].
# Input:  [6,0,8,2,1,5]  →  Output: 4  (i=1, j=5)

def maxWidthRamp(arr):
    pass

# print(maxWidthRamp([6,0,8,2,1,5]))


# ----- EXPRESSION EVALUATION (6 problems) ------------------------------------------------------------------------------------

# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Basic calculator II — evaluate expression with +, -, *, / (no parentheses).
# Input:  "3+2*2"   →  Output: 7
# Input:  " 3/2 "   →  Output: 1
# Input:  " 3+5 / 2 " →  Output: 5

def calculate(s):
    pass

# print(calculate("3+2*2"))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Decode string — decode "k[encoded_string]" patterns.
# Input:  "3[a]2[bc]"   →  Output: "aaabcbc"
# Input:  "3[a2[c]]"    →  Output: "accaccacc"

def decodeString(s):
    pass

# print(decodeString("3[a]2[bc]"))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Score of parentheses — "()" = 1, AB = A+B, (A) = 2*A.
# Input:  "()"       →  Output: 1
# Input:  "(())"     →  Output: 2
# Input:  "(()(()))" →  Output: 6

def scoreParentheses(s):
    pass

# print(scoreParentheses("(()(()))"))


# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Minimum remove to make valid parentheses — remove fewest brackets to make string valid.
# Input:  "lee(t(c)o)de)"  →  Output: "lee(t(c)o)de"
# Input:  "a)b(c)d"        →  Output: "ab(c)d"

def minRemoveParentheses(s):
    pass

# print(minRemoveParentheses("lee(t(c)o)de)"))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Simplify Unix path.
# Input:  "/home//foo/"          →  Output: "/home/foo"
# Input:  "/a/./b/../../c/"      →  Output: "/c"

def simplifyPath(path):
    pass

# print(simplifyPath("/a/./b/../../c/"))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Check if string can be made valid by removing at most 2 bracket characters.
# Input:  "()))"  →  Output: True  (remove 2 closing brackets)
# Input:  "((("   →  Output: True  (remove 1 opening bracket)

def canBeValid(s):
    pass

# print(canBeValid("()))"))


# ----- DEQUE / SLIDING WINDOW QUEUE (8 problems) -----------------------------------------------------------------------------

# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Sliding window maximum — maximum in every window of size k.
# Input:  [1,3,-1,-3,5,3,6,7], k=3  →  Output: [3,3,5,5,6,7]

def slidingWindowMax(nums, k):
    pass

# print(slidingWindowMax([1,3,-1,-3,5,3,6,7], 3))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Design circular queue. Support enQueue, deQueue, Front, Rear, isEmpty, isFull.
# MyCircularQueue(3): enQueue(1)→T, enQueue(2)→T, enQueue(3)→T, enQueue(4)→F, Rear()→3

class MyCircularQueue:
    def __init__(self, k):
        pass
    def enQueue(self, val):
        pass
    def deQueue(self):
        pass
    def Front(self):
        pass
    def Rear(self):
        pass
    def isEmpty(self):
        pass
    def isFull(self):
        pass

# cq = MyCircularQueue(3); cq.enQueue(1); print(cq.Rear())


# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Design circular deque — supports insert/delete from both ends.
# MyCircularDeque(3): insertLast(1)→T, insertLast(2)→T, insertFront(3)→T, insertFront(4)→F

class MyCircularDeque:
    def __init__(self, k):
        pass
    def insertFront(self, val):
        pass
    def insertLast(self, val):
        pass
    def deleteFront(self):
        pass
    def deleteLast(self):
        pass
    def getFront(self):
        pass
    def getRear(self):
        pass
    def isEmpty(self):
        pass
    def isFull(self):
        pass


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Shortest subarray with sum >= k (negatives allowed) — deque + prefix sum.
# Input:  [2,-1,2], k=3  →  Output: 3
# Input:  [1,2], k=4     →  Output: -1

def shortestSubarray(nums, k):
    pass

# print(shortestSubarray([2,-1,2], 3))


# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Jump game VI — maximum score reaching end, each jump up to k steps.
# Input:  nums=[-1,-2,0,3], k=2  →  Output: 3  (path: 0→-1→-1→3=... wait best path: 0→0→3)

def maxResult(nums, k):
    pass

# print(maxResult([-1,-2,0,3], 2))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Constrained subsequence sum — maximum sum of non-empty subsequence, no two elements more than k apart.
# Input:  nums=[10,2,-10,5,20], k=2  →  Output: 37  (10+2+5+20)

def constrainedSubsetSum(nums, k):
    pass

# print(constrainedSubsetSum([10,2,-10,5,20], 2))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Longest continuous subarray with absolute diff <= limit (deque approach).
# Input:  [8,2,4,7], limit=4  →  Output: 2

def longestSubarrayLimit(nums, limit):
    pass

# print(longestSubarrayLimit([8,2,4,7], 4))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum of window in an array at every position of window size k.
# Input:  [1,2,3,1,4,5,2,3,6], k=3  →  Output: [6,6,8,10,11,10,11]  (wrong—just practice deque)

def maxSumWindows(nums, k):
    pass

# print(maxSumWindows([1,2,3,1,4,5,2,3,6], 3))


# ----- BFS QUEUE (6 problems) ------------------------------------------------------------------------------------------------
# These use a queue (collections.deque) to process nodes level by level.

# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Rotting oranges — find minimum minutes for all fresh oranges to rot.
# 0=empty, 1=fresh, 2=rotten. Each minute, rot spreads to adjacent fresh oranges.
# Input:  [[2,1,1],[1,1,0],[0,1,1]]  →  Output: 4
# Input:  [[0,2]]                    →  Output: 0

def orangesRotting(grid):
    pass

# print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# Number of islands — count connected components of '1's in a grid.
# Input:  [["1","1","0"],["0","1","0"],["0","0","1"]]  →  Output: 2

def numIslands(grid):
    pass

# print(numIslands([["1","1","0"],["0","1","0"],["0","0","1"]]))


# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Walls and gates — fill each empty room with distance to nearest gate.
# -1=wall, 0=gate, INF=empty room.
# Input:  [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

def wallsAndGates(rooms):
    pass


# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Task scheduler — given tasks and cooldown n, find minimum intervals to finish all tasks.
# Input:  tasks=["A","A","A","B","B","B"], n=2  →  Output: 8

def leastInterval(tasks, n):
    pass

# print(leastInterval(["A","A","A","B","B","B"], 2))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Design hit counter — count hits in the past 5 minutes (300 seconds).
# hit(1), hit(2), hit(3), getHits(4)→3, hit(300), getHits(300)→4, getHits(301)→3

class HitCounter:
    def __init__(self):
        pass
    def hit(self, timestamp):
        pass
    def getHits(self, timestamp):
        pass

# hc = HitCounter(); hc.hit(1); hc.hit(2); hc.hit(3); print(hc.getHits(4))


# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Open the lock — minimum turns to reach target from "0000", avoiding deadends.
# Input:  deadends=["0201","0101","0102","1212","2002"], target="0202"  →  Output: 6

def openLock(deadends, target):
    pass

# print(openLock(["0201","0101","0102","1212","2002"], "0202"))


# ----- MIXED MEDIUM (4 problems) ---------------------------------------------------------------------------------------------

# [M-33] -----------------------------------------------------------------------------------------------------------------------
# Decode ways II — '*' can be any digit 1-9, count ways modulo 10^9+7.
# Input:  "*"    →  Output: 9
# Input:  "1*"   →  Output: 18

def numDecodingsII(s):
    pass

# print(numDecodingsII("1*"))


# [M-34] -----------------------------------------------------------------------------------------------------------------------
# Longest valid parentheses — length of longest valid bracket substring.
# Input:  "(()"    →  Output: 2
# Input:  ")()())" →  Output: 4

def longestValidParentheses(s):
    pass

# print(longestValidParentheses(")()())"))


# [M-35] -----------------------------------------------------------------------------------------------------------------------
# Check if two bracket sequences can be made equal by swapping.
# Input:  s1=")(", s2="()"  →  Output: True

def canBeEqualBrackets(s1, s2):
    pass

# print(canBeEqualBrackets(")(", "()"))


# [M-36] -----------------------------------------------------------------------------------------------------------------------
# Number of visible people in a queue — for each person, how many can they see to the right?
# Heights are unique. Person i can see person j if no one between them is taller.
# Input:  [10,6,8,5,11,9]  →  Output: [3,1,2,1,1,0]

def canSeePersonsCount(heights):
    pass

# print(canSeePersonsCount([10,6,8,5,11,9]))


# =============================================================================================================================
# HARD (12 problems) — Advanced monotonic stack, DP + stack, complex simulations
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Largest rectangle in histogram (optimised with stack, all edge cases).
# Input:  [2,1,5,6,2,3]  →  Output: 10

def largestRectangleHistogram(heights):
    pass

# print(largestRectangleHistogram([2,1,5,6,2,3]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Maximal rectangle in a binary matrix.
# Input:  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6

def maximalRectangle(matrix):
    pass

# print(maximalRectangle([["1","0","1","0"],["1","0","1","1"],["1","1","1","1"],["1","0","0","1"]]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Basic calculator (with parentheses, +, -, unary minus).
# Input:  "(1+(4+5+2)-3)+(6+8)"  →  Output: 23

def basicCalculator(s):
    pass

# print(basicCalculator("(1+(4+5+2)-3)+(6+8)"))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Maximum frequency stack — push/pop returns the most frequent element (ties: most recent).
# push(5),push(7),push(5),push(7),push(4),push(5) → pop()→5, pop()→7, pop()→5, pop()→4

class FreqStack:
    def __init__(self):
        pass
    def push(self, val):
        pass
    def pop(self):
        pass

# fs = FreqStack()
# for v in [5,7,5,7,4,5]: fs.push(v)
# print([fs.pop() for _ in range(4)])


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Sum of subarray ranges — sum of (max - min) for every subarray.
# Input:  [1,2,3]  →  Output: 4

def subArrayRanges(nums):
    pass

# print(subArrayRanges([1,2,3]))


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# Count of smaller numbers after self — for each element, count how many elements to its right are smaller.
# Input:  [5,2,6,1]  →  Output: [2,1,1,0]

def countSmaller(nums):
    pass

# print(countSmaller([5,2,6,1]))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Remove duplicate letters (lexicographically smallest result, each letter appears once).
# Input:  "bcabc"   →  Output: "abc"
# Input:  "cbacdcbc" →  Output: "acdb"

def removeDuplicateLetters(s):
    pass

# print(removeDuplicateLetters("bcabc"))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Maximum binary tree — build tree where root is max, left subtree from left part, right from right.
# (Return root's value for testing.) Input: [3,2,1,6,0,5] → root = 6

def maxBinaryTree(nums):
    pass

# print(maxBinaryTree([3,2,1,6,0,5]))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# Flatten nested list iterator — implement iterator that flattens [[1,1],2,[1,1]].
# Input:  [[1,1],2,[1,1]]  →  Output: [1,1,2,1,1]

class NestedIterator:
    def __init__(self, nestedList):
        pass
    def next(self):
        pass
    def hasNext(self):
        pass


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Minimum number of swaps to make string balanced — string of '[' and ']'.
# Input:  "][]["  →  Output: 1
# Input:  "]]][[["  →  Output: 2

def minSwaps(s):
    pass

# print(minSwaps("]["))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Stamping the sequence — find order of stamps to reconstruct target string.
# Input:  stamp="abc", target="ababc"  →  Output: [0,2]

def movesToStamp(stamp, target):
    pass

# print(movesToStamp("abc", "ababc"))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Largest rectangle under skyline — same as histogram but given as building widths and heights.
# Input:  buildings=[(2,10),(3,15),(4,12),(1,10),(3,8),(2,20)]  →  Output: area

def largestRectangleSkyline(buildings):
    pass
