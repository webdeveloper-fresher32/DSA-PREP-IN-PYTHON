# ==========================================
# PATTERN PROBLEMS - LOOP MASTERY GUIDE
# ==========================================
# Solve these in order from easiest to hardest
# Each pattern will improve your loop understanding

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
    for i in range(n):
        print("*")

# pattern1(4)


# PATTERN 2: Number Line
# Expected Output:
# 1
# 2
# 3
# 4
def pattern2(n):
    for  i in range(4):
        print(i+1)

# pattern2(4)


# PATTERN 3: Repeated Character
# Expected Output:
# ****
# ****
# ****
# ****
def pattern3(n):
    for i in range(n):
        print("*"* n)

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
    for i in range(n):
        for j in range(n):
            print("*" , end=" ")
        print()

# pattern4(4)


# PATTERN 5: Number Square
# Expected Output (n=4):
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
def pattern5(n):
    for i in range(n):
        for j in range(n):
            print(j+1,end=" ")
        print()

# pattern5(4)


# PATTERN 6: Row Numbers
# Expected Output (n=4):
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
def pattern6(n):
    for i in range(n):
        for j in range(n):
            print(i+1,end=" ")
        print()


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

# For ANY triangle pattern, just change the INNER LOOP RANGE:

# Growing:   range(i+1)           ← More each row
# Shrinking: range(n-i)           ← Less each row
# Fixed:     range(n)             ← Same each row (square)


# formula 
# for i in range(n):           # i = 0, 1, 2, 3
#     for j in range(n):       # j = 0, 1, 2, 3
#         print((i+j+1) * "*") # Prints many stars, wrong!


def pattern7(n):
    for i in range(n):              # i = 0, 1, 2, 3 (row number)
        for j in range(i+1):        # j runs 1, 2, 3, 4 times (columns in each row)
            print("*", end=" ")     # Print star with space
        print()                     # Move to next line after row complete

# pattern7(4)


# PATTERN 8: Number Triangle
# Expected Output (n=4):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
def pattern8(n):
    for i in range(n):
        for j in range(i+1):
            print((i+j+1),end=" ")
        print()

# pattern8(4)


# PATTERN 9: Incremental Triangle
# Expected Output (n=4):
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def pattern9(n):
    for i in range(n):
        for j in range(i+1):
            print((i+1+j),end =" ")
        print()

# pattern9(4)


# PATTERN 10: Reverse Triangle
# Expected Output (n=4):
# * * * *
# * * *
# * *
# *
def pattern10(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()

pattern10(4)


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


# PATTERN 12: Center Pyramid
# Expected Output (n=4):
#    *
#   ***
#  *****
# *******
def pattern12(n):
    pass


# PATTERN 13: Number Pyramid
# Expected Output (n=4):
#    1
#   121
#  12321
# 1234321
def pattern13(n):
    pass


# PATTERN 14: Reverse Pyramid
# Expected Output (n=4):
# * * * *
#  * * *
#   * *
#    *
def pattern14(n):
    pass


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


# PATTERN 19: Alphabet Pattern
# Expected Output (n=4):
# A
# A B
# A B C
# A B C D
def pattern19(n):
    pass


# PATTERN 20: Multiplication Table Pattern
# Expected Output (n=4):
# 1
# 2 4
# 3 6 9
# 4 8 12 16
def pattern20(n):
    pass


# ==========================================
# SOLUTIONS SECTION (Uncomment to see answers)
# ==========================================

# Uncomment below to see solutions gradually

"""
# PATTERN 1 SOLUTION:
def pattern1_solution(n):
    for i in range(n):
        print('*')

# PATTERN 4 SOLUTION:
def pattern4_solution(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

# PATTERN 7 SOLUTION:
def pattern7_solution(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()

# PATTERN 11 SOLUTION:
def pattern11_solution(n):
    for i in range(1, n+1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        print(spaces + stars)

# PATTERN 15 SOLUTION:
def pattern15_solution(n):
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
"""


# ==========================================
# HOW TO USE THIS FILE:
# ==========================================
# 1. Start with PATTERN 1 and solve it
# 2. Test your solution by calling the function
# 3. Move to next pattern
# 4. Try to solve without looking at solutions
# 5. If stuck, uncomment solutions section to see answers
# 6. After solving, try to modify patterns (different symbols, etc)
