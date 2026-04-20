# Matrix Problems — Pattern Recognition Guide

---

## The 5 Core Patterns for Matrix

```
BFS/DFS Traversal    →  islands, spread, shortest path, flood fill
Matrix Manipulation  →  rotate, spiral, transpose, in-place transforms
DP on Matrix         →  paths, min/max sum, squares, falling paths
Prefix Sum 2D        →  rectangle sum queries, submatrix sums
Binary Search        →  search in sorted matrix, kth smallest
```

---

## How to Read a Matrix Problem

Before picking a pattern, identify these three things:

1. **What is the question asking about?**
   - A cell? → Manipulation or DP
   - A region/path? → BFS/DFS or DP
   - A sum? → Prefix Sum
   - A specific value? → Binary Search

2. **Can you move in all 4 directions, or only right/down?**
   - All 4 directions → BFS or DFS
   - Only right/down → DP

3. **Are you counting, finding min/max, or checking existence?**
   - Counting paths → DP
   - Min cost → DP
   - Existence / shortest → BFS
   - Largest connected region → DFS

---

## Pattern 1: BFS / DFS on Matrix

### When to use
- "Number of **islands**" or connected components
- "**Flood fill**" — spread to all connected same-value cells
- **Shortest path** from source to destination in a grid
- **Multi-source spread** (all rotten oranges spread simultaneously)
- "Count cells that **cannot reach** the border"

### DFS vs BFS — which one?
| | DFS | BFS |
|---|---|---|
| Use for | Connected components, flood fill, marking visited regions | Shortest path, minimum steps, multi-source spread |
| Returns | Whether something exists / count of a region | Minimum distance |
| Implementation | Recursion or stack | `collections.deque` |

### Template — DFS (mark visited, explore 4 directions)
```python
def dfs(grid, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    if grid[r][c] != TARGET:
        return
    grid[r][c] = VISITED          # mark in-place to avoid extra visited set
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        dfs(grid, r + dr, c + dc)
```

### Template — BFS (shortest path / multi-source)
```python
from collections import deque
queue = deque()
visited = set()

# Add all sources at once for multi-source BFS
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == SOURCE:
            queue.append((r, c, 0))
            visited.add((r, c))

while queue:
    r, c, dist = queue.popleft()
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            visited.add((nr, nc))
            queue.append((nr, nc, dist + 1))
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-04 | Flood fill |
| M-01 | Number of islands |
| M-02 | Max area of island |
| M-03 | Surrounded regions |
| M-04 | Pacific Atlantic water flow |
| M-05 | Word search |
| M-06 | Rotting oranges |
| M-07 | Shortest path in binary matrix |
| M-08 | Number of enclaves |
| M-11 | Making a large island |

---

## Pattern 2: Matrix Manipulation

### When to use
- Rotating, transposing, or reflecting the matrix
- Generating a matrix with a specific traversal order (spiral)
- In-place transformations based on rules (Game of Life)
- Shifting or reshaping the grid

### Key Tricks

**Rotate 90° clockwise (in-place, 2 steps):**
```
Step 1: Transpose   (swap matrix[i][j] with matrix[j][i])
Step 2: Reverse each row
```

**Rotate 90° counter-clockwise (in-place, 2 steps):**
```
Step 1: Transpose
Step 2: Reverse each column  (or transpose then reverse rows in reverse)
```

**Transpose template:**
```python
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

**Spiral traversal template:**
```python
top, bottom, left, right = 0, rows-1, 0, cols-1
while top <= bottom and left <= right:
    for c in range(left, right + 1):    result.append(matrix[top][c])
    top += 1
    for r in range(top, bottom + 1):    result.append(matrix[r][right])
    right -= 1
    if top <= bottom:
        for c in range(right, left - 1, -1): result.append(matrix[bottom][c])
        bottom -= 1
    if left <= right:
        for r in range(bottom, top - 1, -1): result.append(matrix[r][left])
        left += 1
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-01 | Transpose |
| E-02 | Spiral order traversal |
| M-13 | Rotate image (in-place) |
| M-14 | Spiral matrix II (generate) |
| M-15 | Game of Life |
| M-19 | Shift 2D grid |

---

## Pattern 3: DP on Matrix

### When to use
- "Number of **distinct paths**" from one corner to another
- "**Minimum / maximum sum** path"
- "Largest **square** / rectangle of 1s"
- Movement is restricted (only right/down, or only adjacent)
- Subproblem = answer for a smaller sub-matrix

### Key insight: only right/down movement = DP, not BFS

### Template — Path DP (right/down only)
```python
dp = [[0] * cols for _ in range(rows)]
dp[0][0] = grid[0][0]

for r in range(rows):
    for c in range(cols):
        if r == 0 and c == 0: continue
        from_top  = dp[r-1][c] if r > 0 else float('inf')
        from_left = dp[r][c-1] if c > 0 else float('inf')
        dp[r][c] = grid[r][c] + min(from_top, from_left)
```

### Template — Maximal Square DP
```python
# dp[i][j] = side length of largest square with bottom-right corner at (i,j)
dp = [[0] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '1':
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-21 | Unique paths |
| M-22 | Unique paths II (with obstacles) |
| M-23 | Minimum path sum |
| M-24 | Triangle minimum path |
| M-25 | Maximal square |
| M-26 | Count square submatrices |
| M-28 | Minimum falling path sum |
| H-03 | Dungeon game |
| H-04 | Cherry pickup |

---

## Pattern 4: 2D Prefix Sum

### When to use
- **Multiple range queries** on a static matrix
- "Sum of rectangle" queries
- Counting submatrices with a given sum

### Key formula
```
prefix[i][j] = sum of all elements in rectangle from (0,0) to (i-1,j-1)

prefix[i][j] = matrix[i-1][j-1]
             + prefix[i-1][j]
             + prefix[i][j-1]
             - prefix[i-1][j-1]

Sum of rectangle (r1,c1) to (r2,c2):
= prefix[r2+1][c2+1]
  - prefix[r1][c2+1]
  - prefix[r2+1][c1]
  + prefix[r1][c1]
```

### Template
```python
rows, cols = len(matrix), len(matrix[0])
prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        prefix[i][j] = (matrix[i-1][j-1]
                       + prefix[i-1][j]
                       + prefix[i][j-1]
                       - prefix[i-1][j-1])

def query(r1, c1, r2, c2):
    return (prefix[r2+1][c2+1]
            - prefix[r1][c2+1]
            - prefix[r2+1][c1]
            + prefix[r1][c1])
```

### Problems in this repo
| ID | Problem |
|---|---|
| M-30 | Range sum query 2D |
| M-31 | Count submatrices with all ones |
| M-32 | Maximum sum rectangle |
| H-06 | Count submatrices with sum = target |

---

## Pattern 5: Binary Search on Matrix

### When to use
- Matrix rows and columns are **sorted**
- You need to **search for a value** efficiently
- Finding **kth smallest** in a sorted matrix

### Two types of sorted matrix

**Type 1 — Fully sorted (treat as 1D):**
Each row is sorted. First element of each row > last element of previous row.
→ Convert (mid) to (row, col) using division and modulo.
```python
lo, hi = 0, rows * cols - 1
while lo <= hi:
    mid = (lo + hi) // 2
    val = matrix[mid // cols][mid % cols]
    if val == target: return True
    elif val < target: lo = mid + 1
    else: hi = mid - 1
```

**Type 2 — Row and column sorted (staircase search):**
Start from top-right corner. Move left if too big, move down if too small.
```python
r, c = 0, cols - 1
while r < rows and c >= 0:
    if matrix[r][c] == target: return True
    elif matrix[r][c] > target: c -= 1
    else: r += 1
return False
```

### Problems in this repo
| ID | Problem |
|---|---|
| E-03 | Search in 2D matrix (fully sorted) |
| M-33 | Search in 2D matrix II (row+col sorted) |
| M-34 | Kth smallest in sorted matrix |

---

## Quick Decision Flowchart

```
Read the problem
      │
      ▼
Does it involve connected regions, flooding, or shortest path?
  YES → BFS (shortest path, multi-source) or DFS (count, mark)
  NO  → continue
      │
      ▼
Does it ask to rotate, transpose, or generate in spiral/pattern?
  YES → Matrix Manipulation
  NO  → continue
      │
      ▼
Can movement only go right/down? Optimal substructure?
  YES → DP on Matrix
  NO  → continue
      │
      ▼
Does it ask for sum of a sub-rectangle, possibly multiple queries?
  YES → 2D Prefix Sum
  NO  → continue
      │
      ▼
Is the matrix sorted? Searching for value or kth element?
  YES → Binary Search on Matrix
```

---

## Indexing Cheatsheet

```python
rows = len(matrix)
cols = len(matrix[0])

# 4-directional movement
directions = [(0,1), (0,-1), (1,0), (-1,0)]

# 8-directional movement (includes diagonals)
directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

# Boundary check
def inBounds(r, c):
    return 0 <= r < rows and 0 <= c < cols

# Convert 1D index to 2D
row, col = idx // cols, idx % cols

# Convert 2D to 1D
idx = row * cols + col
```

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Modifying grid while BFS is running | Mark visited before adding to queue, not after popping |
| For "only right/down" paths using BFS | Use DP instead — BFS gives shortest path, not all paths |
| Forgetting base cases in 2D DP | Fill row 0 and col 0 separately before the main loop |
| Rotate in-place but using a copy | Transpose in-place first, then reverse rows in-place |
| DFS stack overflow on large grids | Convert recursion to iterative DFS using explicit stack |

---

## Problem Count Summary

| Level | Count | Focus |
|---|---|---|
| Easy | 16 | Traversal, indexing, basic manipulation |
| Medium | 34 | BFS/DFS, rotation, DP paths, prefix sum, binary search |
| Hard | 12 | Trie+DFS, DP on 2 agents, complex submatrix counting |
| **Total** | **62** | |
