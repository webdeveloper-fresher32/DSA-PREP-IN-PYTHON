# Two Pointer Approach — Pattern Recognition Guide

---

## When to Think "Two Pointers"

Ask yourself these questions when you read a problem:

---

### 1. Is the array (or string) sorted?
If yes → two pointers is almost always worth trying.

> Why: A sorted structure lets you make intelligent decisions about moving left or right, which is what two pointers relies on.

---

### 2. Are you looking for a pair (or triplet) with a target sum?
Keywords: "two numbers that add up to", "pair with sum", "three sum", "four sum"

> Pattern: Place one pointer at start, one at end. If sum is too big → move right pointer left. If too small → move left pointer right.

---

### 3. Are you asked to remove or partition elements in-place?
Keywords: "remove duplicates", "move zeros", "remove element", "partition array"

> Pattern: One pointer tracks the position to write, the other scans forward.

---

### 4. Are you comparing elements from both ends?
Keywords: "palindrome", "reverse", "valid pair from both sides"

> Pattern: Left pointer starts at index 0, right pointer at index n-1. Move inward.

---

### 5. Are you working on a problem with two separate arrays?
Keywords: "merge two sorted arrays", "intersection", "union"

> Pattern: One pointer per array, advance the one with the smaller current value.

---

### 6. Does brute force require a nested loop O(n²) and you need O(n)?
If you wrote (or imagined) a double for loop to check all pairs → that is the signal to reach for two pointers.

---

## Quick Decision Table

| Situation | Two Pointer Type |
|---|---|
| Sorted array, find pair with target sum | Opposite ends |
| Find triplet / four sum | Fix one, opposite ends on rest |
| Remove duplicates in-place | Slow + fast pointer |
| Move zeros / partition | Slow + fast pointer |
| Merge two sorted arrays | One pointer per array |
| Palindrome check | Opposite ends |
| Container with most water | Opposite ends |

---

## Two Pointer Variants

### Opposite Ends (most common)
```
left = 0
right = len(arr) - 1
while left < right:
    # make a decision and move one pointer
```
Use when: sorted array, pair sum, palindrome, container problems.

---

### Slow + Fast (same direction)
```
slow = 0
for fast in range(len(arr)):
    # slow writes, fast scans
```
Use when: remove duplicates, move zeros, partition problems.

---

### Two Arrays
```
i = 0
j = 0
while i < len(a) and j < len(b):
    # compare a[i] and b[j], advance the smaller
```
Use when: merge sorted arrays, intersection, union.

---

## Red Flags That It Is NOT Two Pointers

- Array is unsorted and sorting it changes the answer → think hashing instead
- You need the actual subarray (not just a pair) → think sliding window
- Problem involves frequency counting → think hashing
- You need prefix/suffix information → think prefix sum

---

## Problems in This Repo That Use Two Pointers

| Problem ID | Name |
|---|---|
| M-01 | Pair sum in sorted array |
| M-02 | Two sum (unsorted — use hashing, not two pointers) |
| M-03 | Three sum |
| M-04 | Container with most water |
| M-05 | Sort colors (Dutch National Flag) |
| M-06 | Four sum |
| M-07 | Remove element |
| M-08 | Merge sorted arrays |
| M-09 | Find the duplicate |
| M-10 | Rearrange by sign |
| E-01 | Reverse array |
| E-13 | Remove duplicates from sorted array |
| E-12 | Move zeros |
