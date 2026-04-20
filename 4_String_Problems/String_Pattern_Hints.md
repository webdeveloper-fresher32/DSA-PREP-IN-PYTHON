# String Problems — Pattern Recognition Guide

---

## The 5 Core Patterns for Strings

```
Sliding Window  →  substrings, longest/shortest window, distinct chars
Two Pointers    →  palindromes, comparing ends, reversals
Hashing         →  frequency, anagrams, character mapping
Stack           →  brackets, undo/delete, nested structures
DP              →  matching, edit distance, palindrome partitioning
```

---

## Pattern 1: Sliding Window

### When to use
Ask yourself:
- Does the problem involve a **substring** (contiguous portion)?
- Does the problem ask for **"longest"**, **"shortest"**, **"minimum window"**?
- Is there a constraint on **distinct characters** or **character frequency**?
- Does it involve **"at most k"**, **"exactly k"**, or **"contains all of"**?

If yes to any → **Sliding Window**

### Keywords that trigger it
> "longest substring", "smallest window", "at most k distinct",
> "permutation in string", "all anagrams in", "minimum window containing"

### The two flavours

**Fixed-size window** — window size k never changes
```python
# Use when: max/min of every window of fixed size k
for i in range(len(s)):
    window.add(s[i])
    if len(window) > k:
        window.remove(s[i - k])
    # check answer at each step
```

**Variable-size window** — window shrinks when constraint is violated
```python
left = 0
for right in range(len(s)):
    # expand: add s[right] to window
    while <constraint violated>:
        # shrink: remove s[left] from window
        left += 1
    # window [left..right] is valid — check answer
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-01 | Longest substring without repeating characters |
| M-02 | Longest substring with at most k distinct chars |
| M-03 | Permutation in string |
| M-04 | Find all anagrams in a string |
| M-05 | Longest repeating character replacement |
| M-06 | Max consecutive ones III |
| M-07 | Number of substrings containing all a,b,c |
| M-09 | Minimum window substring |
| M-11 | Substrings with exactly k distinct chars |

---

## Pattern 2: Two Pointers

### When to use
- String is being **compared from both ends** (palindrome checks)
- You need to **reverse** part of a string in-place
- You are comparing **two strings** side by side character by character
- Brute force would be O(n²) and you want O(n)

### Keywords that trigger it
> "palindrome", "reverse", "valid after one deletion",
> "compare", "two sorted strings", "meeting in the middle"

### Template — Opposite Ends
```python
left, right = 0, len(s) - 1
while left < right:
    # make decision, move one or both pointers
    left += 1
    right -= 1
```

### Template — Slow + Fast (same direction)
```python
slow = 0
for fast in range(len(s)):
    if <condition>:
        s[slow] = s[fast]
        slow += 1
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-02 | Is palindrome |
| M-13 | Valid palindrome II |
| M-14 | Reverse vowels |
| M-15 | Reverse only letters |
| M-16 | Backspace string compare |
| M-17 | Longest palindromic substring |
| M-18 | Count palindromic substrings |

---

## Pattern 3: Hashing (dict / set)

### When to use
- You need to count **character frequencies**
- You need to detect **duplicates** or **anagrams**
- You are **mapping** characters from one string to another
- You need to look something up in **O(1)**

### Keywords that trigger it
> "anagram", "isomorphic", "frequency", "first unique",
> "group by", "pattern match", "seen before"

### Template — Frequency Count
```python
from collections import Counter
freq = Counter(s)
```

### Template — Character Mapping (isomorphic)
```python
s_to_t = {}
t_to_s = {}
for cs, ct in zip(s, t):
    if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
        return False
    s_to_t[cs] = ct
    t_to_s[ct] = cs
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-04 | Is anagram |
| E-05 | First non-repeating character |
| E-18 | Ransom note |
| M-19 | Group anagrams |
| M-20 | Isomorphic strings |
| M-21 | Word pattern |
| M-23 | Find duplicate words |
| M-24 | Top k frequent words |

---

## Pattern 4: Stack

### When to use
- Problem involves **brackets / parentheses** (open/close matching)
- There is a **undo / delete previous** character behaviour (`#` backspace)
- Problem has **nested structure** ("decode 3[a2[c]]")
- You need to find the **nearest boundary** to the left or right

### Keywords that trigger it
> "valid parentheses", "decode", "remove adjacent duplicates",
> "backspace", "score of", "nested", "undo"

### Template
```python
stack = []
for ch in s:
    if <opening condition>:
        stack.append(ch)
    elif stack and <closing condition>:
        stack.pop()
    else:
        stack.append(ch)
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-16 | Valid parentheses |
| M-29 | Decode string |
| M-30 | Remove adjacent duplicates |
| M-31 | Remove k digits |
| M-32 | Simplify path |
| M-33 | Score of parentheses |
| M-34 | Longest valid parentheses |

---

## Pattern 5: Dynamic Programming (DP)

### When to use
- Problem asks for **minimum operations** between two strings
- Problem asks **"can this string be formed from / match another"**
- Problem involves **counting ways** or **checking if possible**
- Palindrome problems with **partitioning** or **counting all substrings**

### Keywords that trigger it
> "edit distance", "minimum operations", "matching", "subsequence",
> "interleaving", "decode ways", "count ways", "word break"

### Template — 2D DP (edit distance style)
```python
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
# fill base cases, then fill table row by row
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-28 | Number of ways to decode a string |
| H-02 | Regular expression matching |
| H-03 | Wildcard matching |
| H-04 | Edit distance |
| H-05 | Interleaving string |
| H-06 | Distinct subsequences |
| H-07 | Palindrome partitioning II |
| H-10 | Word break |

---

## Quick Decision Flowchart

```
Read the problem
      │
      ▼
Is it about a substring (contiguous)?
  YES → Sliding Window
  NO  → continue
      │
      ▼
Are you comparing from both ends or reversing?
  YES → Two Pointers
  NO  → continue
      │
      ▼
Do you need frequency, mapping, or lookup?
  YES → Hashing
  NO  → continue
      │
      ▼
Is there nesting, undo, or bracket matching?
  YES → Stack
  NO  → continue
      │
      ▼
Does it ask "minimum ops", "can be formed", "count ways"?
  YES → DP
```

---

## Red Flags to Avoid Mistakes

| Situation | Don't use | Use instead |
|---|---|---|
| Unsorted, find pair | Two Pointers | Hashing |
| Contiguous substring needed | Hashing alone | Sliding Window |
| Nested / recursive structure | Two Pointers | Stack |
| "Can be formed" / "min steps" | Sliding Window | DP |

---

## How Strings Differ from Arrays

| Aspect | Array | String |
|---|---|---|
| Elements | integers | characters (a-z, A-Z, digits) |
| Frequency map size | unbounded | at most 26 (lowercase) |
| In-place edit | easy | convert to list first in Python |
| Sliding window | same technique | same technique |
| Key extra tool | prefix sum | character frequency window |

> In Python: `list(s)` to edit in-place, `"".join(lst)` to convert back.

---

## Problem Count Summary

| Level | Count | Focus |
|---|---|---|
| Easy | 18 | Basics, loops, hashing |
| Medium | 38 | Sliding Window, Two Pointers, Hashing, Stack |
| Hard | 12 | DP, advanced matching, Manacher's |
| **Total** | **68** | |
