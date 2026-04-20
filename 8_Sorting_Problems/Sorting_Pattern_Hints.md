# Sorting — Pattern Recognition Guide

---

## Why Sorting Matters Beyond "Sort the Array"

Sorting is rarely the final answer — it is a **pre-processing step** that unlocks a faster solution.
When you see a problem that seems to need O(n²) brute force, ask:
> "If I sort first, does a greedy or two-pointer solution become obvious?"

That question solves more than half of all medium sorting problems.

---

## The 6 Patterns

```
Sorting Algorithms    →  know the mechanics, time/space, when each shines
Merge Sort Based      →  count inversions, merge k sorted, reverse pairs
Quick Select          →  kth largest/smallest in O(n) average
Custom Comparator     →  sort by a rule you define (largest number, log files)
Counting/Bucket Sort  →  O(n) sort when range is known or bounded
Sort + Greedy         →  sort first, then make optimal greedy choices
```

---

## Algorithm Reference Card

| Algorithm | Best | Average | Worst | Space | Stable? | Use when |
|---|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Teaching only |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Minimise swaps |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Nearly sorted, small n |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Linked lists, stable sort needed |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | General purpose, cache-friendly |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Guaranteed O(n log n), O(1) space |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Range is small and known |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | Large integers, fixed-length strings |

> k = range of values (Counting Sort), k = number of digits (Radix Sort)

---

## Pattern 1: Sorting Algorithm Implementations

### Merge Sort Template
```python
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

### Quick Sort Template
```python
def quickSort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p - 1)
        quickSort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1
```

### Heap Sort Template
```python
import heapq
def heapSort(arr):
    heapq.heapify(arr)                         # min-heap in O(n)
    return [heapq.heappop(arr) for _ in arr]   # pop n times in O(n log n)
```

---

## Pattern 2: Merge Sort Based Problems

### When to use
- "Count **inversions**" (pairs where left > right)
- "Count **reverse pairs**" (arr[i] > 2*arr[j])
- "Count of **smaller numbers** after self"
- Any problem where the relationship between left-half and right-half elements matters during merge

### Key insight
During the merge step, when you take an element from the RIGHT array, every remaining element in the LEFT array is greater than it.
That gap is where you count inversions, reverse pairs, etc.

### Template — Count Inversions
```python
def countInversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left,  lc = countInversions(arr[:mid])
    right, rc = countInversions(arr[mid:])
    merged = []
    count = lc + rc
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            count += len(left) - i    # all remaining left elements > right[j]
    merged += left[i:] + right[j:]
    return merged, count
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-06 | Count inversions |
| M-07 | Merge k sorted arrays |
| M-10 | Count reverse pairs |
| H-01 | Count of smaller numbers after self |
| H-02 | Reverse pairs |
| H-03 | Count of range sum |

---

## Pattern 3: Quick Select

### When to use
- "Kth **largest** element"
- "Kth **smallest** element"
- "Top k **frequent** elements"
- Any kth-order statistic problem where O(n log n) is too slow

### Key insight
Quick sort partitions around a pivot. Quick select does the same but recurses into **only one side** — giving O(n) average time.

### Template
```python
import random

def quickSelect(nums, k):
    # returns kth largest
    pivot = random.choice(nums)
    left   = [x for x in nums if x > pivot]   # greater than pivot
    middle = [x for x in nums if x == pivot]
    right  = [x for x in nums if x < pivot]   # less than pivot

    if k <= len(left):
        return quickSelect(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quickSelect(right, k - len(left) - len(middle))
```

### Python built-in shortcut
```python
# For competitive problems where O(n log n) is acceptable:
nums.sort()
return nums[-k]        # kth largest

# Using heapq for top-k:
import heapq
heapq.nlargest(k, nums)[-1]     # kth largest
heapq.nsmallest(k, nums)[-1]    # kth smallest
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-12 | Kth largest element |
| M-13 | Kth smallest element |
| M-14 | Top k frequent elements |
| M-15 | Kth largest in stream |

---

## Pattern 4: Custom Comparator

### When to use
- The sort order is **not natural** (not just ascending/descending)
- "Largest number formed by concatenation"
- "Sort by X, then by Y as tiebreaker"
- "Letter-logs before digit-logs"

### Template — Python custom sort
```python
from functools import cmp_to_key

# Option 1: key function (preferred when possible)
arr.sort(key=lambda x: some_transform(x))

# Option 2: comparator function (use when comparison is complex)
def compare(a, b):
    if a_should_come_first: return -1
    elif b_should_come_first: return 1
    else: return 0

arr.sort(key=cmp_to_key(compare))
```

### Largest Number trick
```python
from functools import cmp_to_key
def compare(a, b):
    if a + b > b + a: return -1   # a should come first
    elif a + b < b + a: return 1
    return 0
nums_str = list(map(str, nums))
nums_str.sort(key=cmp_to_key(compare))
```

### Multi-key sort
```python
# Sort by score descending, then name ascending
students.sort(key=lambda x: (-x[1], x[0]))
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-16 | Largest number |
| M-17 | Wiggle sort |
| M-19 | Sort students |
| M-20 | Reorder log files |
| M-22 | Sort by number of 1-bits |

---

## Pattern 5: Counting / Bucket Sort

### When to use
- Values are in a **known bounded range** [0, k]
- k is small enough to allocate k buckets
- Need **O(n) sort** (comparison sort can't beat O(n log n))

### Template — Counting Sort
```python
def countingSort(arr, max_val):
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    result = []
    for val, freq in enumerate(count):
        result.extend([val] * freq)
    return result
```

### Template — Bucket Sort (for floats in [0,1))
```python
def bucketSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for x in arr:
        buckets[int(x * n)].append(x)
    for bucket in buckets:
        bucket.sort()
    return [x for bucket in buckets for x in bucket]
```

### Maximum Gap trick (bucket sort for O(n) gap finding)
```python
# Pigeonhole: if n numbers span range [min, max],
# max gap >= ceil((max-min)/(n-1))
# Place each number in a bucket of that size.
# Max gap must span across buckets — compare adjacent bucket boundaries.
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-04 | Counting sort implementation |
| M-05 | Radix sort implementation |
| M-23 | Maximum gap |
| M-24 | Top k frequent words |
| M-26 | Find all duplicates (index marking) |

---

## Pattern 6: Sort + Greedy

### When to use
- Problem asks for **minimum**, **maximum**, or **optimal** assignment
- After sorting, the greedy choice at each step is **obviously correct**
- Interval problems (merge, schedule, partition)
- Resource allocation (platforms, workers, machines)

### The mental model
> Sort → removes the burden of "which element to process next" → greedy picks become easy

### Interval sorting rules
| Goal | Sort by |
|---|---|
| Merge overlapping intervals | Start time ascending |
| Maximum non-overlapping intervals | End time ascending (activity selection) |
| Minimum rooms / platforms needed | Start time, then use a min-heap for end times |
| Minimum intervals to remove | End time ascending |

### Template — Merge Intervals
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

### Template — Minimum Meeting Rooms
```python
import heapq
intervals.sort(key=lambda x: x[0])
heap = []   # stores end times of ongoing meetings
for start, end in intervals:
    if heap and heap[0] <= start:
        heapq.heapreplace(heap, end)
    else:
        heapq.heappush(heap, end)
return len(heap)
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-27 | Merge intervals |
| M-28 | Non-overlapping intervals |
| M-29 | Meeting rooms II |
| M-30 | Minimum platforms |
| M-31 | Activity selection |
| M-32 | Two city scheduling |
| M-33 | Minimum cost to connect ropes |

---

## Quick Decision Flowchart

```
Read the problem
      │
      ▼
Does it ask you to implement a specific sort algorithm?
  YES → Sorting Algorithm Implementation
  NO  → continue
      │
      ▼
Does it involve counting inversions, reverse pairs, or merging sorted structures?
  YES → Merge Sort Based
  NO  → continue
      │
      ▼
Does it ask for kth largest / kth smallest?
  YES → Quick Select (or heap if streaming)
  NO  → continue
      │
      ▼
Is the sorting rule non-standard (concatenation, log-type, bit-count)?
  YES → Custom Comparator
  NO  → continue
      │
      ▼
Are values in a small known range? Need O(n) time?
  YES → Counting Sort or Bucket Sort
  NO  → continue
      │
      ▼
Does sorting first make a greedy or two-pointer solution obvious?
  YES → Sort + Greedy
```

---

## The "Sort First" Heuristic

When stuck, try: **what if I sort the array first?**

| Problem looks like | After sorting it becomes |
|---|---|
| Find pair with target sum | Two pointers from both ends |
| Merge overlapping intervals | Scan left to right, extend current |
| Assign tasks to minimise cost | Pick cheapest available option each time |
| Find kth largest | Just index from end |
| Count inversions | Merge sort detects them naturally |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using built-in sort when O(n log n) is too slow | Check if counting/bucket sort applies |
| Quick sort on already-sorted input → O(n²) | Always randomise pivot: `random.choice(arr)` |
| Forgetting stable sort matters | Python's `sort()` is stable (Timsort); use `key=` to preserve relative order |
| Wrong comparator direction | Test with two elements manually before submitting |
| Merge sort space: creating new arrays on every call | Pass indices instead of slicing for O(1) extra merge overhead |

---

## Python Cheatsheet

```python
# Sort in-place
arr.sort()                          # ascending
arr.sort(reverse=True)              # descending
arr.sort(key=lambda x: x[1])        # by second element

# Sort and return new list
sorted_arr = sorted(arr)
sorted_arr = sorted(arr, key=abs)   # by absolute value

# Custom comparator
from functools import cmp_to_key
arr.sort(key=cmp_to_key(lambda a, b: -1 if a > b else 1))

# Heap (min-heap by default)
import heapq
heapq.heapify(arr)                  # O(n) — converts list to heap in-place
heapq.heappush(arr, val)
heapq.heappop(arr)                  # returns and removes smallest
heapq.nlargest(k, arr)              # k largest elements
heapq.nsmallest(k, arr)             # k smallest elements

# Max-heap: negate values
heapq.heappush(arr, -val)
-heapq.heappop(arr)
```

---

## Problem Count Summary

| Level | Count | Focus |
|---|---|---|
| Easy | 16 | Algorithm implementations, basic sort-based |
| Medium | 34 | Merge sort based, quick select, custom sort, greedy |
| Hard | 12 | Count inversions, sliding median, heap-based optimisation |
| **Total** | **62** | |
