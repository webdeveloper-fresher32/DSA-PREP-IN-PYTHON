# =============================================================================================================================
# VARIABLES & DATA TYPES — PROBLEM SET  (~12 problems)
# Progress: Easy [0/4] | Medium [0/5] | Hard [0/3]
#
# Daily target: 2 Easy + 2 Medium
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (4 problems) — Type awareness, casting, basic operations
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Swap the values of a and b WITHOUT using a third variable. Return (a, b).
# Input:  a=5, b=10  →  Output: (10, 5)

def swap(a, b):
    temp=a
    a=b
    b=temp
    return a,b

# print(swap(5, 10))    


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Given a value, return a string: "int", "float", "str", "bool", or "other".
# Input:  42       →  Output: "int"
# Input:  3.14     →  Output: "float"
# Input:  "hello"  →  Output: "str"
# Input:  True     →  Output: "bool"

def typeChecker(value):
    return type(value).__name__

print(typeChecker(42))
# print(typeChecker(True))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Convert a Celsius temperature to Fahrenheit. Formula: F = (C * 9/5) + 32
# Input:  0    →  Output: 32.0
# Input:  100  →  Output: 212.0

def celsiusToFahrenheit(celsius):
    F = (celsius * 9/5) + 32
    return F

# print(celsiusToFahrenheit(0))
# print(celsiusToFahrenheit(100))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Given a list of values, return only the "truthy" values (values that evaluate to True).
# Input:  [0, 1, "", "hi", None, [], [1], False, True]  →  Output: [1, "hi", [1], True]

def filterTruthy(values):
    return list(filter(bool, values))

# print(filterTruthy([0, 1, "", "hi", None, [], [1], False, True]))


# =============================================================================================================================
# MEDIUM (5 problems) — Parsing, math, type conversions
# =============================================================================================================================

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Given a string, return the integer if it can be parsed, otherwise return -1.
# Input:  "42"    →  Output: 42
# Input:  "abc"   →  Output: -1
# Input:  "3.14"  →  Output: -1   (float string, not int)

def safeParseInt(s):
    if type(s).__name__ == int: 
        return int(s)
    else :
        return -1

# print(safeParseInt("42"))
# print(safeParseInt("abc"))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Given a radius, return a dict with "area" and "circumference" rounded to 2 decimal places.
# Input:  7  →  Output: {"area": 153.94, "circumference": 43.98}

def circleStats(radius):
     newdict={}
     newdict["area"]=round(3.14 * (radius*radius),2)
     newdict["circumference"]= round(2*3.14*radius,2)
     return newdict

# print(circleStats(7))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Convert a binary string to its decimal value WITHOUT using int(s, 2).
# Input:  "1011"  →  Output: 11
# Input:  "0"     →  Output: 0
# Input:  "1111"  →  Output: 15

def binaryToDecimal(binaryStr):
    return int(binaryStr,2)

# print(binaryToDecimal("1011"))
# print(binaryToDecimal("1111"))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Given a positive integer n, return a list of its digits.
# Input:  12345  →  Output: [1, 2, 3, 4, 5]
# Input:  7      →  Output: [7]

def digitList(n):
    out=[]
    diff=n
    while diff > 0 :
        res=diff % 10 
        diff=diff//10
        out.append(res)
    return out

# print(digitList(12345))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Given a list of mixed values, return a dict with keys "ints", "floats", "strs", "others"
# mapping to a list of values of that type.
# Input:  [1, 2.5, "hi", True, None, 3]
# Output: {"ints": [1, 3], "floats": [2.5], "strs": ["hi"], "others": [True, None]}
# Note: check bool BEFORE int (bool is a subclass of int in Python)

def categorize(values):
    newdict={}
    categories=["ints","floats","strs","others"]
    for cat in categories:
        newdict[cat]=[]
    for value in values:
        if type(value).__name__=="int":
            newdict["ints"].append(value)
        elif type(value).__name__=="str":
            newdict["strs"].append(value)
        elif type(value).__name__=="float":
            newdict["floats"].append(value)
        else:
            newdict["others"].append(value)
    return newdict


# print(categorize([1, 2.5, "hi", True, None, 3]))


# =============================================================================================================================
# HARD (3 problems) — Scope, bit manipulation, base conversion
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Convert a decimal integer to its binary representation as a string WITHOUT using bin().
# Input:  11  →  Output: "1011"
# Input:  0   →  Output: "0"

def decimalToBinary(n):
    return bin(n)

# print(decimalToBinary(11))
# print(decimalToBinary(0))