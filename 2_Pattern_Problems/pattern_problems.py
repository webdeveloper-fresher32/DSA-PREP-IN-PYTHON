# ==========================================
# PATTERN PROBLEMS - LOOP MASTERY GUIDE
# ==========================================
# Solve these in order from easiest to hardest
# Each pattern will improve your loop understanding

# ==========================================
# UNIVERSAL FORMULAS FOR PATTERN PROBLEMS
# ==========================================

# TRIANGLE PATTERNS - Change inner loop range:
# ─────────────────────────────────────────
# Growing Triangle:   for j in range(i+1)        ← More each row (1, 2, 3, 4...)
# Shrinking Triangle: for j in range(n-i)        ← Less each row (4, 3, 2, 1...)
# Fixed/Square:       for j in range(n)          ← Same each row

# PYRAMID PATTERNS - Spacing + Logic:
# ─────────────────────────────────────
# for i in range(1, n+1):
#     # 1. Leading spaces
#     print(" " * (n - i), end="")
#
#     # 2. Left part (increasing)
#     for j in range(...):
#         print(..., end="")
#
#     # 3. Right part (decreasing)
#     for j in range(...):
#         print(..., end="")
#
#     print()  # New line after row

# DIAMOND PATTERNS - Upper + Lower Half:
# ───────────────────────────────────────
# for i in range(1, n+1):        # Upper half: 1 to n
#     (pyramid logic here)
# for i in range(n-1, 0, -1):    # Lower half: n-1 to 1
#     (same pyramid logic)

# CHARACTER CONVERSION:
# ─────────────────────
# Numbers → Letters: chr(65 + j) = A, B, C... (65 = ASCII 'A')
#                    chr(97 + j) = a, b, c... (97 = ASCII 'a')

# ==========================================
# LEVEL 1: BASIC PATTERNS (1 loop)
# ==========================================

# PATTERN 1: Simple Square
# Expected Output:
# *
# *
# *
# *
def pattern1(n):
    pass

# pattern1(4)


# PATTERN 2: Number Line
# Expected Output:
# 1
# 2
# 3
# 4
def pattern2(n):
    pass

# pattern2(4)


# PATTERN 3: Repeated Character
# Expected Output:
# ****
# ****
# ****
# ****
def pattern3(n):
    pass

# pattern3(4)


# ==========================================
# LEVEL 2: SIMPLE NESTED PATTERNS
# ==========================================

# PATTERN 4: Square Grid
# Expected Output (n=4):
# * * * *
# * * * *
# * * * *
# * * * *

# Pattern where you print something inside nested loop:
# for i in range(n):           # ROWS
#     for j in range(n):       # COLUMNS
#         print(something, end=" ")  # Print in same row
#     print()                  # Move to next row


def pattern4(n):
    pass

# pattern4(4)


# PATTERN 5: Number Square
# Expected Output (n=4):
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
def pattern5(n):
    pass

# pattern5(4)


# PATTERN 6: Row Numbers
# Expected Output (n=4):
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
def pattern6(n):
    pass

# pattern6(4)


# ==========================================
# LEVEL 3: TRIANGLES (Conditional Logic)
# ==========================================

# PATTERN 7: Right Triangle
# Expected Output (n=4):
# *
# * *
# * * *
# * * * *
def pattern7(n):
    pass

# pattern7(4)


# PATTERN 8: Number Triangle
# Expected Output (n=4):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
def pattern8(n):
    pass

# pattern8(4)


# PATTERN 9: Incremental Triangle
# Expected Output (n=4):
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def pattern9(n):
    pass

# pattern9(4)


# PATTERN 10: Reverse Triangle
# Expected Output (n=4):
# * * * *
# * * *
# * *
# *
def pattern10(n):
    pass

# pattern10(4)


# ==========================================
# LEVEL 4: PYRAMIDS (Spacing + Logic)
# ==========================================

# PATTERN 11: Left Pyramid
# Expected Output (n=4):
#    *
#   **
#  ***
# ****
def pattern11(n):
    pass

# pattern11(4)


# PATTERN 12: Center Pyramid
# Expected Output (n=4):
#    *
#   ***
#  *****
# *******
def pattern12(n):
    pass

# pattern12(4)


# PATTERN 13: Number Pyramid
# Expected Output (n=4):
#    1
#   121
#  12321
# 1234321
def pattern13(n):
    pass

# pattern13(4)


# PATTERN 14: Reverse Pyramid
# Expected Output (n=4):
# * * * *
#  * * *
#   * *
#    *
def pattern14(n):
    pass

# pattern14(4)


# ==========================================
# LEVEL 5: DIAMONDS (Complex Logic)
# ==========================================

# PATTERN 15: Diamond
# Expected Output (n=4):
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def pattern15(n):
    pass

# pattern15(4)


# PATTERN 16: Hollow Diamond
# Expected Output (n=4):
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
def pattern16(n):
    pass

# pattern16(4)


# PATTERN 17: Number Diamond
# Expected Output (n=4):
#    1
#   212
#  32123
# 4321234
#  32123
#   212
#    1
def pattern17(n):
    pass

# pattern17(4)


# ==========================================
# LEVEL 6: ADVANCED PATTERNS
# ==========================================

# PATTERN 18: Butterfly
# Expected Output (n=4):
# *        *
# **      **
# ***    ***
# ****  ****
# ****  ****
# ***    ***
# **      **
# *        *
def pattern18(n):
    pass

# pattern18(4)


# PATTERN 19: Alphabet Pattern
# Expected Output (n=4):
# A
# A B
# A B C
# A B C D
def pattern19(n):
    pass

# pattern19(4)


# PATTERN 20: Multiplication Table Pattern
# Expected Output (n=4):
# 1
# 2 4
# 3 6 9
# 4 8 12 16
def pattern20(n):
    pass

# pattern20(4)
