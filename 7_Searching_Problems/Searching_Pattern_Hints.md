# Searching (Binary Search) — Pattern Recognition Guide

---

## The Single Most Important Insight

> Binary search is not just "search in sorted array."
> It is: **eliminate half the search space at every step.**

If you can define a space where:
- One half definitely does NOT contain the answer
- The other half might

→ Binary search applies. The array doesn't even need to be sorted.

---

## The 5 Patterns

```
Classic BS            →  sorted array, find value or insertion point
Finding Boundaries    →  first/last occurrence, floor, ceil, peak
Rotated/Modified      →  rotated sorted array, bitonic, nearly sorted
BS on Answer Space    →  "minimum maximum", "maximum minimum", feasibility check
2D Binary Search      →  sorted matrix, kth smallest
```

---

## Pattern 1: Classic Binary Search

### When to use
- Array is **sorted** (ascending or descending)
- You are searching for a **specific value**
- You need the **insertion position**

### The one template to memorise
```python
def binarySearch(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2    # avoids overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

> Always use `mid = lo + (hi - lo) // 2`, not `(lo + hi) // 2`.
> Same result, but avoids integer overflow in languages like Java/C++.

---

## Pattern 2: Finding Boundaries

### When to use
- Find **first occurrence** (leftmost) of a value
- Find **last occurrence** (rightmost) of a value
- Find **floor** (largest value ≤ target)
- Find **ceil** (smallest value ≥ target)
- Find **peak element** (greater than both neighbours)

### Template — First Occurrence (left boundary)
```python
def firstOccurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1    # keep going LEFT to find first
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
```

### Template — Last Occurrence (right boundary)
```python
def lastOccurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1    # keep going RIGHT to find last
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
```

### Template — Peak Element
```python
def findPeak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid        # peak is in left half (including mid)
        else:
            lo = mid + 1    # peak is in right half
    return lo
```

---

## Pattern 3: Rotated / Modified Sorted Array

### When to use
- Array was sorted but then **rotated** (some pivot point)
- Array is **bitonic** (increases then decreases)
- Every element appears twice except one (**single non-duplicate**)
- Array is **nearly sorted** (elements shifted ±1)

### Key insight for rotated array
At any mid point, one of the two halves is always fully sorted.
Use that half to decide which side to eliminate.

### Template — Search in Rotated Array
```python
def searchRotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        # left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

### Template — Single Non-Duplicate (pairs break pattern)
```python
def singleNonDuplicate(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid % 2 == 1:
            mid -= 1            # always check even index
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2        # pair intact → single is to the right
        else:
            hi = mid            # pair broken → single is here or left
    return nums[lo]
```

---

## Pattern 4: Binary Search on Answer Space (MOST IMPORTANT MEDIUM/HARD PATTERN)

### What is it?
Instead of searching FOR a value IN an array, you:
1. Define the **range of possible answers** [lo, hi]
2. Write a **feasibility function** `canAchieve(mid)` that returns True/False
3. Binary search over the answer space to find the boundary

### When to use — the trigger questions
- "**Minimum** possible **maximum**" (minimise the largest)
- "**Maximum** possible **minimum**" (maximise the smallest)
- "**Minimum time/speed/days** to achieve something"
- Problem gives you a constraint (k workers, D days, m students)
- Brute force is: try every possible answer → O(n²) or worse

### Keywords that trigger it
> "minimum maximum", "maximum minimum",
> "koko eating bananas", "ship packages in D days",
> "allocate books", "aggressive cows", "painter's partition",
> "minimum days", "minimum speed"

### The Universal Template
```python
def solve(arr, constraint):
    def canAchieve(mid):
        # check if 'mid' is a feasible answer given the constraint
        # returns True if feasible, False otherwise
        pass

    lo = min_possible_answer
    hi = max_possible_answer
    result = hi

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if canAchieve(mid):
            result = mid        # mid works, try smaller (for minimise)
            hi = mid - 1
        else:
            lo = mid + 1        # mid doesn't work, need larger

    return result
```

### How to set lo and hi
| Problem type | lo | hi |
|---|---|---|
| Min eating speed | 1 | max(piles) |
| Ship in D days | max(weights) | sum(weights) |
| Allocate books | max(books) | sum(books) |
| Aggressive cows | 1 | max(stalls) - min(stalls) |
| Painter's partition | max(boards) | sum(boards) |

> **Rule of thumb:** lo = minimum conceivably valid answer, hi = worst case (everything in one unit)

### Worked example — Koko Eating Bananas
```python
def minEatingSpeed(piles, h):
    def canFinish(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h
        # same as: ceil(p / speed) for each pile

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if canFinish(mid):
            hi = mid        # speed works, try slower
        else:
            lo = mid + 1    # too slow, need faster
    return lo
```

---

## Pattern 5: Binary Search on 2D Matrix

### Two types — completely different approaches

**Type 1: Fully sorted (first element of row > last of previous row)**
Treat the matrix as a 1D sorted array.
```python
lo, hi = 0, rows * cols - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    val = matrix[mid // cols][mid % cols]   # convert 1D index to 2D
    if val == target: return True
    elif val < target: lo = mid + 1
    else: hi = mid - 1
```

**Type 2: Row + column sorted (staircase search) — O(m+n), not O(log n)**
Start at top-right. Move left if too big, down if too small.
```python
r, c = 0, cols - 1
while r < rows and c >= 0:
    if matrix[r][c] == target: return True
    elif matrix[r][c] > target: c -= 1
    else: r += 1
return False
```

---

## Quick Decision Flowchart

```
Read the problem
      │
      ▼
Is there a sorted array and you need to find a value?
  YES → Classic Binary Search
  NO  → continue
      │
      ▼
Do you need first/last occurrence, floor, ceil, or peak?
  YES → Finding Boundaries (modified BS with result variable)
  NO  → continue
      │
      ▼
Is the array rotated, bitonic, or has single non-duplicate?
  YES → Rotated/Modified Binary Search
  NO  → continue
      │
      ▼
Does the problem say "minimum maximum" / "maximum minimum"
or give you a constraint (k workers, D days)?
  YES → Binary Search on Answer Space
  NO  → continue
      │
      ▼
Is it a 2D sorted matrix?
  YES → Fully sorted → 1D trick | Row+col sorted → staircase
```

---

## How to Recognise "BS on Answer" in Disguise

These problem descriptions all hide a BS on Answer pattern:

| What it says | What it means |
|---|---|
| "Koko eats bananas in h hours" | Binary search on eating speed |
| "Ship packages within D days" | Binary search on ship capacity |
| "Place k cows maximising distance" | Binary search on minimum distance |
| "Allocate books to m students" | Binary search on max pages |
| "k workers finish in minimum time" | Binary search on time |
| "Cut ribbons to get k pieces" | Binary search on piece length |

**Pattern to spot:** problem has a number `k` or `D` that acts as a constraint, and you return a size/speed/distance/capacity.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| `while lo < hi` vs `while lo <= hi` | Use `<= ` when looking for exact match; use `<` for boundary search where lo converges to answer |
| Off-by-one: `hi = mid` vs `hi = mid - 1` | If `mid` can be the answer, use `hi = mid`. If not, use `hi = mid - 1` |
| Wrong lo/hi for BS on answer | lo = min valid answer (not 0), hi = max valid answer (not infinity) |
| Infinite loop when `lo = hi - 1` with `hi = mid` | If using `hi = mid`, ensure `mid = lo + (hi - lo) // 2` (rounds down) |
| Forgetting to handle duplicates in rotated array | Add `lo++` when `arr[lo] == arr[mid] == arr[hi]` to skip duplicates |

---

## Python Cheatsheet

```python
import bisect

# bisect_left: index of first element >= target (left boundary)
bisect.bisect_left(arr, target)

# bisect_right: index of first element > target (right boundary)
bisect.bisect_right(arr, target)

# Count occurrences using bisect
count = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)

# Insert in sorted order
bisect.insort(arr, val)
```

---

## Problem Count Summary

| Level | Count | Focus |
|---|---|---|
| Easy | 16 | Classic search, boundaries, floor/ceil |
| Medium | 32 | Rotated arrays, BS on answer, 2D matrix |
| Hard | 12 | Median of arrays, kth pair distance, real-valued BS |
| **Total** | **60** | |
