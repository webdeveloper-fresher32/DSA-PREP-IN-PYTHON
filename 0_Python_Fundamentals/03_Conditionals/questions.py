# =============================================================================================================================
# CONDITIONALS — PROBLEM SET  (~12 problems)
# Progress: Easy [0/4] | Medium [0/5] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# Patterns: Basic if/elif/else | Guard Clauses | Multi-Condition Logic | Edge Cases
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Simple branching logic
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Given a score (0-100), return the letter grade.
# 90-100 → "A" | 80-89 → "B" | 70-79 → "C" | 60-69 → "D" | below 60 → "F"
# Input:  95  →  Output: "A"
# Input:  55  →  Output: "F"

def getGrade(score):
    pass

# print(getGrade(95))
# print(getGrade(55))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Return True if the year is a leap year, False otherwise.
# Rules: divisible by 4, BUT NOT by 100, UNLESS also by 400.
# Input:  2000  →  Output: True
# Input:  1900  →  Output: False
# Input:  2024  →  Output: True

def isLeapYear(year):
    pass

# print(isLeapYear(2000))
# print(isLeapYear(1900))
# print(isLeapYear(2024))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# A cinema charges based on age:
# Under 12 → $8 | 12-17 → $12 | 18-64 → $15 | 65+ → $10
# Input:  10  →  Output: 8
# Input:  30  →  Output: 15

def ticketPrice(age):
    pass

# print(ticketPrice(10))
# print(ticketPrice(70))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Given weight (kg) and height (m), compute BMI = weight / height^2. Return category:
# BMI < 18.5 → "Underweight" | 18.5-24.9 → "Normal" | 25-29.9 → "Overweight" | 30+ → "Obese"
# Input:  50, 1.7   →  Output: "Underweight"
# Input:  70, 1.75  →  Output: "Normal"

def bmiCategory(weight, height):
    pass

# print(bmiCategory(50, 1.7))
# print(bmiCategory(70, 1.75))


# =============================================================================================================================
# MEDIUM (5 problems) — Multi-condition logic, edge cases
# =============================================================================================================================

# ----- VALIDATION LOGIC (3 problems) -----------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Given three sides a, b, c, classify the triangle:
# - "equilateral" if all sides equal
# - "isosceles"   if exactly two sides equal
# - "scalene"     if all sides different
# - "invalid"     if any side >= sum of the other two
# Input:  5, 5, 5  →  Output: "equilateral"
# Input:  1, 2, 10 →  Output: "invalid"

def triangleType(a, b, c):
    pass

# print(triangleType(5, 5, 5))
# print(triangleType(3, 4, 5))
# print(triangleType(1, 2, 10))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# A valid password must:
# - Be at least 8 characters long
# - Contain at least one uppercase letter
# - Contain at least one lowercase letter
# - Contain at least one digit
# - Contain at least one special character from: !@#$%^&*
# Return True if valid, False otherwise.
# Input:  "Abc!1234"   →  Output: True
# Input:  "abc12345"   →  Output: False  (no uppercase, no special char)

def isValidPassword(password):
    pass

# print(isValidPassword("Abc!1234"))
# print(isValidPassword("abc12345"))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Given player1 and player2 choices ("rock", "paper", "scissors"),
# return "Player 1 wins", "Player 2 wins", or "Draw".
# Try to solve WITHOUT nested if-else — use a set or dict approach.
# Input:  "rock", "scissors"  →  Output: "Player 1 wins"
# Input:  "paper", "paper"    →  Output: "Draw"

def rockPaperScissors(player1, player2):
    pass

# print(rockPaperScissors("rock", "scissors"))
# print(rockPaperScissors("paper", "paper"))


# ----- EDGE CASE HANDLING (2 problems) ---------------------------------------------------------------------------------------

# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Given year, month (1-12), and day, return True if the date is valid.
# Account for: days in each month, leap years for February.
# Input:  2024, 2, 29  →  Output: True   (2024 is a leap year)
# Input:  2023, 2, 29  →  Output: False
# Input:  2023, 4, 31  →  Output: False  (April has 30 days)

def isValidDate(year, month, day):
    pass

# print(isValidDate(2024, 2, 29))
# print(isValidDate(2023, 2, 29))
# print(isValidDate(2023, 4, 31))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Implement a simple calculator. Given two numbers and an operator string ("+","-","*","/"),
# return the result. Handle division by zero by returning None.
# Input:  10, 2, "/"  →  Output: 5.0
# Input:  10, 0, "/"  →  Output: None
# Input:  3, 4, "+"   →  Output: 7

def calculator(a, b, operator):
    pass

# print(calculator(10, 2, "/"))
# print(calculator(10, 0, "/"))
# print(calculator(3, 4, "+"))


# =============================================================================================================================
# HARD (3 problems) — Complex branching, simulation, multi-rule systems
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Tax calculator. Given income, apply UK-style tax brackets:
# 0-12570      →  0%   (Personal Allowance)
# 12571-50270  →  20%  (Basic Rate)
# 50271-125140 →  40%  (Higher Rate)
# Above 125140 →  45%  (Additional Rate)
# Return total tax owed (rounded to 2 decimal places).
# Input:  60000  →  Output: 11492.0   (0 + 7540 + 3952)

def calculateTax(income):
    pass

# print(calculateTax(60000))
# print(calculateTax(12000))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Given a list of integers, return:
# - "All positive"  if every number > 0
# - "All negative"  if every number < 0
# - "All zero"      if every number == 0
# - "Mixed"         otherwise
# Input:  [1, 2, 3]    →  Output: "All positive"
# Input:  [-1, 0, 1]   →  Output: "Mixed"

def classifyList(nums):
    pass

# print(classifyList([1, 2, 3]))
# print(classifyList([-1, 0, 1]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Implement a simple vending machine. Given a list of (item, price) tuples and
# an amount inserted, return a list of all items the user can afford (price <= amount).
# Sort by price ascending. If none affordable, return [].
# Input:  [("chips",1.5),("water",1.0),("cola",2.0)], amount=1.5
# Output: ["water", "chips"]

def vendingMachine(items, amount):
    pass

# print(vendingMachine([("chips",1.5),("water",1.0),("cola",2.0)], 1.5))
# print(vendingMachine([("chips",1.5),("water",1.0)], 0.5))
