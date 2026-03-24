# 🎯 PATTERN PRINTING FORMULAS - COMPLETE GUIDE

## BASIC FORMULAS

### 1️⃣ SIMPLE SQUARE (Fixed Grid)

```python
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

**Formula:** Inner loop = `range(n)` (always n iterations)
**Output (n=4):**

```
* * * *
* * * *
* * * *
* * * *
```

---

## TRIANGLE FORMULAS

### 2️⃣ RIGHT TRIANGLE (Growing)

```python
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
```

**Formula:** Inner loop = `range(i+1)` (increases: 1,2,3,4...)
**Output (n=4):**

```
*
* *
* * *
* * * *
```

### 3️⃣ REVERSE TRIANGLE (Shrinking)

```python
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
```

**Formula:** Inner loop = `range(n-i)` (decreases: 4,3,2,1...)
**Output (n=4):**

```
* * * *
* * *
* *
*
```

### 4️⃣ NUMBER TRIANGLE

```python
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```

**Formula:** Inner loop = `range(1, i+1)` (prints 1 to i)
**Output (n=4):**

```
1
1 2
1 2 3
1 2 3 4
```

### 5️⃣ INCREMENTAL TRIANGLE (Floyd's Triangle)

```python
counter = 1
for i in range(1, n+1):
    for j in range(i):
        print(counter, end=" ")
        counter += 1
    print()
```

**Formula:** Use a counter variable that increments continuously
**Output (n=4):**

```
1
2 3
4 5 6
7 8 9 10
```

---

## PYRAMID FORMULAS (With Spacing)

### 6️⃣ LEFT PYRAMID

```python
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * i
    print(spaces + stars)
```

**Formula:**

- Spaces = `' ' * (n - i)` (decreases)
- Stars = `'*' * i` (increases)

**Output (n=4):**

```
   *
  **
 ***
****
```

### 7️⃣ CENTER PYRAMID (Wide)

```python
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * (2*i - 1)
    print(spaces + stars)
```

**Formula:**

- Spaces = `' ' * (n - i)` (decreases)
- Stars = `'*' * (2*i - 1)` (1,3,5,7...)

**Output (n=4):**

```
   *
  ***
 *****
*******
```

### 8️⃣ REVERSE PYRAMID

```python
for i in range(n, 0, -1):
    spaces = ' ' * (n - i)
    stars = '*' * i
    print(spaces + stars)
```

**Formula:** Loop from `range(n, 0, -1)` (counts down)
**Output (n=4):**

```
****
 ***
  **
   *
```

---

## DIAMOND FORMULAS

### 9️⃣ DIAMOND (Perfect)

```python
# Upper half
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * (2*i - 1)
    print(spaces + stars)
# Lower half
for i in range(n-1, 0, -1):
    spaces = ' ' * (n - i)
    stars = '*' * (2*i - 1)
    print(spaces + stars)
```

**Formula:** Upper half + lower half (reversed)
**Output (n=4):**

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

### 🔟 HOLLOW DIAMOND

```python
# Upper half
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    if i == 1:
        print(spaces + '*')
    else:
        inside = ' ' * (2*i - 3)
        print(spaces + '*' + inside + '*')
# Lower half
for i in range(n-1, 0, -1):
    spaces = ' ' * (n - i)
    if i == 1:
        print(spaces + '*')
    else:
        inside = ' ' * (2*i - 3)
        print(spaces + '*' + inside + '*')
```

**Formula:** Check if edge (i==1 or i==n), else print hollow
**Output (n=4):**

```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

---

## ROW/COLUMN NUMBER PATTERNS

### 1️⃣1️⃣ NUMBER SQUARE (Same across rows)

```python
for i in range(n):
    for j in range(n):
        print(j+1, end=" ")
    print()
```

**Formula:** Print `j+1` (column number repeats)
**Output (n=4):**

```
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
```

### 1️⃣2️⃣ ROW NUMBER SQUARE (Same down columns)

```python
for i in range(n):
    for j in range(n):
        print(i+1, end=" ")
    print()
```

**Formula:** Print `i+1` (row number repeats)
**Output (n=4):**

```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

### 1️⃣3️⃣ MULTIPLICATION TABLE PATTERN

```python
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()
```

**Formula:** Print `i*j` (row × col)
**Output (n=4):**

```
1
2 4
3 6 9
4 8 12 16
```

---

## ADVANCED PATTERNS

### 1️⃣4️⃣ BUTTERFLY PATTERN

```python
# Upper half
for i in range(1, n+1):
    left = '*' * i
    spaces = ' ' * (2*(n-i))
    right = '*' * i
    print(left + spaces + right)
# Lower half
for i in range(n, 0, -1):
    left = '*' * i
    spaces = ' ' * (2*(n-i))
    right = '*' * i
    print(left + spaces + right)
```

**Formula:** Left stars + middle spaces + right stars
**Output (n=4):**

```
*        *
**      **
***    ***
****  ****
****  ****
***    ***
**      **
*        *
```

### 1️⃣5️⃣ ALPHABET TRIANGLE

```python
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()
```

**Formula:**

- Inner loop = `range(i+1)` (growing)
- Print `chr(65+j)` (ASCII: A=65, B=66...)

**Output (n=4):**

```
A
A B
A B C
A B C D
```

### 1️⃣6️⃣ REVERSE ALPHABET TRIANGLE

```python
for i in range(n):
    for j in range(i+1):
        print(chr(65+i-j), end=" ")
    print()
```

**Formula:** Print `chr(65+i-j)` (counts down)
**Output (n=4):**

```
A
B A
C B A
D C B A
```

### 1️⃣7️⃣ STAIRCASE PATTERN

```python
for i in range(n):
    spaces = ' ' * i
    stars = '*' * (n-i)
    print(spaces + stars)
```

**Formula:**

- Spaces = `' ' * i` (increases)
- Stars = `'*' * (n-i)` (decreases)

**Output (n=4):**

```
****
 ***
  **
   *
```

---

## 📊 QUICK REFERENCE TABLE

| Pattern            | Inner Loop     | Spaces | Stars/Numbers | Use Case           |
| ------------------ | -------------- | ------ | ------------- | ------------------ |
| Square             | `range(n)`     | None   | Fixed         | Grid               |
| Growing Triangle   | `range(i+1)`   | None   | Increasing    | Right triangle     |
| Shrinking Triangle | `range(n-i)`   | None   | Decreasing    | Reverse triangle   |
| Left Pyramid       | `range(1,i+1)` | `n-i`  | `i`           | Centered left      |
| Center Pyramid     | `range(1,i+1)` | `n-i`  | `2*i-1`       | Diamond-like       |
| Diamond            | `range(1,n+1)` | `n-i`  | `2*i-1`       | Full diamond       |
| Alphabet           | `range(i+1)`   | None   | `chr(65+j)`   | Letter patterns    |
| Floyd's            | `range(i)`     | None   | Counter++     | Sequential numbers |

---

## 🎯 FORMULA BREAKDOWN CHEAT SHEET

```python
# OUTER LOOP OPTIONS:
range(n)           # Normal: 0,1,2,3...
range(1, n+1)      # Skip 0: 1,2,3,4...
range(n, 0, -1)    # Reverse: n,n-1,...1

# INNER LOOP OPTIONS:
range(n)           # Fixed: same every row
range(i+1)         # Growing: increases with row
range(n-i)         # Shrinking: decreases with row
range(1, i+1)      # Growing from 1: 1,2,3...

# SPACING FORMULA:
spaces = ' ' * (n-i)       # Decreasing
spaces = ' ' * i           # Increasing

# STARS FORMULA:
stars = '*' * i            # Linear: 1,2,3,4...
stars = '*' * (2*i-1)      # Odd: 1,3,5,7...
stars = '*' * (n-i)        # Reverse: n,n-1...
```

---

## 💡 HOW TO APPROACH ANY PATTERN

1. **Count rows and columns** - What's the pattern?
2. **Identify outer loop** - `range(n)` or `range(n, 0, -1)`?
3. **Identify inner loop** - `range(n)` or `range(i+1)` or `range(n-i)`?
4. **Add spacing** - Do you need leading spaces?
5. **Calculate what to print** - Stars? Numbers? Letters?
6. **Test with small n** - Use n=3 or n=4 to verify

---

## 🚀 PRACTICE ORDER

1. Square (Pattern 4)
2. Right Triangle (Pattern 7)
3. Reverse Triangle (Pattern 10)
4. Left Pyramid (Pattern 11)
5. Center Pyramid (Pattern 12)
6. Diamond (Pattern 15)
7. Hollow Diamond (Pattern 16)
8. Alphabet Triangle (Pattern 19)
9. Butterfly (Pattern 18)
10. Floyd's Triangle (Pattern 9)

Master these and you'll never struggle with nested loops again! 🎉
