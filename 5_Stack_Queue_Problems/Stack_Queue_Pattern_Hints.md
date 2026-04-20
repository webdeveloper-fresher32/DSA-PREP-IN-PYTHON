# Stacks & Queues — Pattern Recognition Guide

---

## The 5 Core Patterns

```
Monotonic Stack      →  next/prev greater/smaller, histogram, span
Bracket Matching     →  valid parentheses, nested structures, undo
Expression Eval      →  calculator, decode, path simplification
Deque (Sliding Win)  →  sliding window max/min, shortest subarray
BFS Queue            →  grid problems, level-by-level traversal
```

---

## Pattern 1: Monotonic Stack

### What is it?
A stack that is always kept in sorted order (increasing or decreasing).
Every time you push, you pop elements that violate the order first.

### When to use
- "Find the **next greater/smaller** element"
- "Find the **previous greater/smaller** element"
- "How many days until temperature is **warmer**"
- "**Span** of prices" (how many consecutive days price was ≤ today)
- "**Histogram** — largest rectangle"
- Problems involving **domination** (asteroids, buildings blocking view)

### Keywords that trigger it
> "next greater", "next smaller", "daily temperatures", "stock span",
> "sum of subarray min/max", "largest rectangle", "visible people"

### Two flavours

**Increasing stack** (bottom → top goes up) → finds next/prev SMALLER
```python
stack = []  # stores indices
for i in range(len(arr)):
    while stack and arr[stack[-1]] >= arr[i]:   # pop larger elements
        stack.pop()
    result[i] = arr[stack[-1]] if stack else -1  # prev smaller
    stack.append(i)
```

**Decreasing stack** (bottom → top goes down) → finds next/prev GREATER
```python
stack = []  # stores indices
for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:    # pop smaller elements
        idx = stack.pop()
        result[idx] = arr[i]                    # next greater for popped
    stack.append(i)
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-01 | Daily temperatures |
| M-02 | Next greater element II (circular) |
| M-03 | Online stock span |
| M-04 | Sum of subarray minimums |
| M-05 | Remove k digits |
| M-06 | Asteroid collision |
| M-07 | 132 pattern |
| M-08 | Previous smaller element |
| M-09 | Next smaller element |
| M-10 | Largest rectangle in histogram |
| M-11 | Trapping rain water |
| M-36 | Number of visible people in queue |

---

## Pattern 2: Bracket Matching

### When to use
- String contains `( ) { } [ ]` and you need to check validity
- There is an **undo / delete previous** operation (`#` backspace, `C` remove last)
- You need to find the **depth** or **score** of nested brackets
- You need to **remove minimum brackets** to make string valid

### Keywords that trigger it
> "valid parentheses", "balanced brackets", "minimum remove",
> "score of", "longest valid", "undo", "backspace"

### Template — Classic Matching
```python
stack = []
matching = {')': '(', '}': '{', ']': '['}
for ch in s:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if not stack or stack[-1] != matching[ch]:
            return False
        stack.pop()
return len(stack) == 0
```

### Template — Track Indices (for minimum remove)
```python
stack = []   # stores indices of unmatched '('
remove = set()
for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        if stack:
            stack.pop()
        else:
            remove.add(i)
remove |= set(stack)
return ''.join(ch for i, ch in enumerate(s) if i not in remove)
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-03 | Valid parentheses |
| M-15 | Score of parentheses |
| M-16 | Minimum remove to make valid |
| M-34 | Longest valid parentheses |
| H-03 | Basic calculator (with parentheses) |

---

## Pattern 3: Expression Evaluation

### When to use
- You need to evaluate a **mathematical expression** as a string
- Problem involves **operator precedence** (+, -, *, /)
- There are **nested encoded structures** like `3[a2[c]]`
- **Path-like** strings need simplification (Unix paths with `.` and `..`)

### Keywords that trigger it
> "calculate", "evaluate expression", "decode string",
> "simplify path", "reverse polish", "postfix"

### Template — Calculator II (no parentheses)
```python
stack = []
num = 0
sign = '+'
for i, ch in enumerate(s):
    if ch.isdigit():
        num = num * 10 + int(ch)
    if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
        if sign == '+':   stack.append(num)
        elif sign == '-': stack.append(-num)
        elif sign == '*': stack.append(stack.pop() * num)
        elif sign == '/': stack.append(int(stack.pop() / num))
        sign = ch
        num = 0
return sum(stack)
```

### Template — Decode String
```python
stack = []
curr_str = ""
curr_num = 0
for ch in s:
    if ch.isdigit():
        curr_num = curr_num * 10 + int(ch)
    elif ch == '[':
        stack.append((curr_str, curr_num))
        curr_str, curr_num = "", 0
    elif ch == ']':
        prev_str, num = stack.pop()
        curr_str = prev_str + num * curr_str
    else:
        curr_str += ch
return curr_str
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-15 | Evaluate RPN (postfix) |
| M-13 | Basic calculator II |
| M-14 | Decode string |
| M-17 | Simplify path |
| H-03 | Basic calculator (with parentheses) |

---

## Pattern 4: Deque (Double-Ended Queue)

### When to use
- **Sliding window maximum or minimum** — need to query max/min of a window in O(1)
- Window is moving and you need to **drop stale elements from the front**
- You need to **add elements to the front OR back**
- Combines monotonic idea with a queue (elements expire by index)

### Keywords that trigger it
> "sliding window maximum", "maximum in window", "shortest subarray with sum >= k",
> "at most k steps apart", "constrained subsequence"

### Template — Sliding Window Maximum
```python
from collections import deque
dq = deque()   # stores indices, front is always the max
result = []
for i in range(len(nums)):
    # remove indices outside window
    while dq and dq[0] < i - k + 1:
        dq.popleft()
    # remove smaller elements from back (they can never be max)
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        result.append(nums[dq[0]])
return result
```

### Stack vs Deque — Key Difference
| | Stack | Deque |
|---|---|---|
| Add/remove | one end only (top) | both ends |
| Use case | monotonic problems, matching | sliding window, BFS |
| Python | `list` with `.append`/`.pop` | `collections.deque` |

### Problems in this repo
| ID | Problem |
|---|---|
| M-19 | Sliding window maximum |
| M-22 | Shortest subarray with sum >= k |
| M-23 | Jump game VI |
| M-24 | Constrained subsequence sum |
| M-25 | Longest subarray with abs diff <= limit |

---

## Pattern 5: BFS Queue

### When to use
- **Grid problems** where you spread from multiple sources simultaneously
- You need the **shortest path** in an unweighted graph
- Process nodes **level by level** (tree or graph)
- Find **minimum steps / minimum time** to reach a state

### Keywords that trigger it
> "minimum steps", "shortest path", "level by level",
> "spread from all sources at once", "minimum time", "rotting", "walls and gates"

### Template — Multi-source BFS
```python
from collections import deque
queue = deque()
visited = set()

# Add all starting points at once
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == SOURCE:
            queue.append((r, c, 0))   # (row, col, distance)
            visited.add((r, c))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
while queue:
    r, c, dist = queue.popleft()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
            visited.add((nr, nc))
            queue.append((nr, nc, dist + 1))
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-27 | Rotting oranges |
| M-28 | Number of islands |
| M-29 | Walls and gates |
| M-32 | Open the lock |

---

## Quick Decision Flowchart

```
Read the problem
      │
      ▼
Does it ask for next/prev greater or smaller? Span? Histogram?
  YES → Monotonic Stack
  NO  → continue
      │
      ▼
Does it involve brackets, undo, or nested structure matching?
  YES → Bracket Matching Stack
  NO  → continue
      │
      ▼
Does it involve evaluating an expression or decoding?
  YES → Expression Eval Stack
  NO  → continue
      │
      ▼
Does it need max/min of a moving window efficiently?
  YES → Deque (Monotonic Queue)
  NO  → continue
      │
      ▼
Is it a grid/graph problem needing shortest path or level spread?
  YES → BFS Queue
```

---

## Stack vs Queue — When to Use Which

| Use Stack when... | Use Queue when... |
|---|---|
| You need LIFO (last in, first out) | You need FIFO (first in, first out) |
| Processing needs to be reversed | Processing order must be preserved |
| Undo / backtrack | Spread outward from sources |
| Nested depth (brackets, decode) | Level-by-level traversal |
| "Most recent" matters | "Earliest" matters |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Using a plain list as queue (pop from front is O(n)) | Use `collections.deque` with `popleft()` |
| Forgetting to handle remaining elements in stack after loop | After the main loop, process what's left in the stack |
| Off-by-one in sliding window deque (stale index check) | Check `dq[0] < i - k + 1` not `<= ` |
| Monotonic stack — not sure increasing or decreasing? | Ask: do I need next GREATER → decreasing stack; next SMALLER → increasing stack |

---

## Python Cheatsheet

```python
# Stack
stack = []
stack.append(x)    # push
stack.pop()        # pop from top
stack[-1]          # peek top

# Queue (always use deque, NOT list)
from collections import deque
queue = deque()
queue.append(x)    # enqueue at right
queue.popleft()    # dequeue from left
queue[0]           # peek front

# Deque (double-ended)
dq = deque()
dq.append(x)       # add right
dq.appendleft(x)   # add left
dq.pop()           # remove right
dq.popleft()       # remove left
```

---

## Problem Count Summary

| Level | Count | Focus |
|---|---|---|
| Easy | 17 | Stack/queue mechanics, valid brackets, basic structures |
| Medium | 36 | Monotonic stack, expression eval, deque, BFS |
| Hard | 12 | Advanced monotonic, DP+stack, complex simulations |
| **Total** | **65** | |
