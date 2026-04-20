# =============================================================================================================================
# MATRIX — COMPLETE PROBLEM SET  (~62 problems)
# Progress: Easy [0/16] | Medium [0/34] | Hard [0/12]
#
# Daily target: 1 Easy + 2 Medium
# Patterns: BFS/DFS Traversal | Matrix Manipulation | DP on Matrix | Prefix Sum | Binary Search
# Solved = uncomment the print test at the bottom of each problem
# =============================================================================================================================


# =============================================================================================================================
# EASY (16 problems) — Traversal, basic manipulation, comfort with row/col indexing
# =============================================================================================================================

# [E-01] -----------------------------------------------------------------------------------------------------------------------
# Transpose a matrix — swap rows and columns.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

def transpose(matrix):
    pass

# print(transpose([[1,2,3],[4,5,6],[7,8,9]]))


# [E-02] -----------------------------------------------------------------------------------------------------------------------
# Spiral order traversal — return all elements in spiral (clockwise) order.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [1,2,3,6,9,8,7,4,5]

def spiralOrder(matrix):
    pass

# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))


# [E-03] -----------------------------------------------------------------------------------------------------------------------
# Search in a 2D matrix — each row sorted, first element of row > last of previous row.
# Input:  matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3  →  Output: True

def searchMatrix(matrix, target):
    pass

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


# [E-04] -----------------------------------------------------------------------------------------------------------------------
# Flood fill — fill connected region of same colour with new colour.
# Input:  image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

def floodFill(image, sr, sc, color):
    pass

# print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))


# [E-05] -----------------------------------------------------------------------------------------------------------------------
# Set matrix zeroes — if element is 0, set its entire row and column to 0 in-place.
# Input:  [[1,1,1],[1,0,1],[1,1,1]]  →  Output: [[1,0,1],[0,0,0],[1,0,1]]

def setZeroes(matrix):
    pass

# print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))


# [E-06] -----------------------------------------------------------------------------------------------------------------------
# Count number of 1s in a binary matrix.
# Input:  [[1,0,1],[0,1,0],[1,1,1]]  →  Output: 6

def countOnes(matrix):
    pass

# print(countOnes([[1,0,1],[0,1,0],[1,1,1]]))


# [E-07] -----------------------------------------------------------------------------------------------------------------------
# Diagonal traversal — traverse all diagonals top-right to bottom-left alternately.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [1,2,4,7,5,3,6,8,9]

def diagonalTraversal(matrix):
    pass

# print(diagonalTraversal([[1,2,3],[4,5,6],[7,8,9]]))


# [E-08] -----------------------------------------------------------------------------------------------------------------------
# Anti-diagonal sum — sum of each anti-diagonal (top-right to bottom-left).
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [1, 6, 15, 14, 9]  (sums of diags)

def antiDiagonalSums(matrix):
    pass

# print(antiDiagonalSums([[1,2,3],[4,5,6],[7,8,9]]))


# [E-09] -----------------------------------------------------------------------------------------------------------------------
# Boundary traversal — collect all border elements in clockwise order.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [1,2,3,6,9,8,7,4]

def boundaryTraversal(matrix):
    pass

# print(boundaryTraversal([[1,2,3],[4,5,6],[7,8,9]]))


# [E-10] -----------------------------------------------------------------------------------------------------------------------
# Check if matrix is symmetric (equal to its transpose).
# Input:  [[1,2,3],[2,5,6],[3,6,9]]  →  Output: True

def isSymmetric(matrix):
    pass

# print(isSymmetric([[1,2,3],[2,5,6],[3,6,9]]))


# [E-11] -----------------------------------------------------------------------------------------------------------------------
# Find row with maximum number of 1s in a row-wise sorted binary matrix.
# Input:  [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]  →  Output: 2

def rowWithMaxOnes(matrix):
    pass

# print(rowWithMaxOnes([[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]))


# [E-12] -----------------------------------------------------------------------------------------------------------------------
# Matrix rotation check — is matrix B a 90/180/270 degree rotation of matrix A?
# Input:  A=[[1,2],[3,4]], B=[[3,1],[4,2]]  →  Output: True  (90° rotation)

def isRotation(A, B):
    pass

# print(isRotation([[1,2],[3,4]], [[3,1],[4,2]]))


# [E-13] -----------------------------------------------------------------------------------------------------------------------
# Pascal's triangle — generate first n rows as a 2D matrix.
# Input:  n=5  →  Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def generatePascal(n):
    pass

# print(generatePascal(5))


# [E-14] -----------------------------------------------------------------------------------------------------------------------
# Sum of all elements in a matrix.
# Input:  [[1,2],[3,4]]  →  Output: 10

def matrixSum(matrix):
    pass

# print(matrixSum([[1,2],[3,4]]))


# [E-15] -----------------------------------------------------------------------------------------------------------------------
# Toeplitz matrix — every diagonal from top-left to bottom-right has the same elements.
# Input:  [[1,2,3,4],[5,1,2,3],[9,5,1,2]]  →  Output: True

def isToeplitzMatrix(matrix):
    pass

# print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))


# [E-16] -----------------------------------------------------------------------------------------------------------------------
# Reshape a matrix — reshape m×n matrix into r×c. If impossible, return original.
# Input:  matrix=[[1,2],[3,4]], r=1, c=4  →  Output: [[1,2,3,4]]

def matrixReshape(matrix, r, c):
    pass

# print(matrixReshape([[1,2],[3,4]], 1, 4))


# =============================================================================================================================
# MEDIUM (34 problems) — BFS/DFS | Matrix Manipulation | DP | Prefix Sum | Binary Search
# =============================================================================================================================

# ----- BFS / DFS ON MATRIX (12 problems) -------------------------------------------------------------------------------------

# [M-01] -----------------------------------------------------------------------------------------------------------------------
# Number of islands — count connected components of '1's.
# Input:  [["1","1","0"],["0","1","0"],["0","0","1"]]  →  Output: 2

def numIslands(grid):
    pass

# print(numIslands([["1","1","0"],["0","1","0"],["0","0","1"]]))


# [M-02] -----------------------------------------------------------------------------------------------------------------------
# Max area of island — find the largest island (connected 1s).
# Input:  [[0,0,1,0],[0,1,1,0],[0,1,0,0],[0,0,0,1]]  →  Output: 4

def maxAreaOfIsland(grid):
    pass

# print(maxAreaOfIsland([[0,0,1,0],[0,1,1,0],[0,1,0,0],[0,0,0,1]]))


# [M-03] -----------------------------------------------------------------------------------------------------------------------
# Surrounded regions — flip all 'O' regions not connected to the border to 'X'.
# Input:  [["X","X","X"],["X","O","X"],["X","X","X"]]
# Output: [["X","X","X"],["X","X","X"],["X","X","X"]]

def surroundedRegions(board):
    pass

# print(surroundedRegions([["X","X","X"],["X","O","X"],["X","X","X"]]))


# [M-04] -----------------------------------------------------------------------------------------------------------------------
# Pacific Atlantic water flow — find cells that can flow to both oceans.
# Water flows to neighbour if neighbour height <= current height.
# Input:  [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

def pacificAtlantic(heights):
    pass

# print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


# [M-05] -----------------------------------------------------------------------------------------------------------------------
# Word search — check if word exists in the grid following adjacent cells (no reuse).
# Input:  board=[["A","B","C"],["S","F","C"],["A","D","E"]], word="ABCCED"  →  Output: True

def wordSearch(board, word):
    pass

# print(wordSearch([["A","B","C"],["S","F","C"],["A","D","E"]], "ABCCED"))


# [M-06] -----------------------------------------------------------------------------------------------------------------------
# Rotting oranges — minimum minutes for all fresh oranges to rot (multi-source BFS).
# Input:  [[2,1,1],[1,1,0],[0,1,1]]  →  Output: 4

def orangesRotting(grid):
    pass

# print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


# [M-07] -----------------------------------------------------------------------------------------------------------------------
# Shortest path in binary matrix — shortest path from top-left to bottom-right (0=open, 1=blocked).
# Input:  [[0,1],[1,0]]  →  Output: 2
# Input:  [[0,0,0],[1,1,0],[1,1,0]]  →  Output: 4

def shortestPathBinaryMatrix(grid):
    pass

# print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))


# [M-08] -----------------------------------------------------------------------------------------------------------------------
# Number of enclaves — count land cells that cannot reach the border.
# Input:  [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]  →  Output: 3

def numEnclaves(grid):
    pass

# print(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))


# [M-09] -----------------------------------------------------------------------------------------------------------------------
# Count distinct islands — count islands where shape is unique (not just count).
# Input:  [[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,1,0]]  →  Output: 2

def numDistinctIslands(grid):
    pass

# print(numDistinctIslands([[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,1,0]]))


# [M-10] -----------------------------------------------------------------------------------------------------------------------
# Minimum steps to reach target from source in a grid with obstacles.
# Source=(0,0), target=(r,c), 0=open, 1=blocked.
# Input:  grid=[[0,0,0],[0,1,0],[0,0,0]], target=(2,2)  →  Output: 4

def minStepsToTarget(grid, target):
    pass

# print(minStepsToTarget([[0,0,0],[0,1,0],[0,0,0]], (2,2)))


# [M-11] -----------------------------------------------------------------------------------------------------------------------
# Making a large island — flip at most one 0 to 1 to make the largest island.
# Input:  [[1,0],[0,1]]  →  Output: 3

def largestIsland(grid):
    pass

# print(largestIsland([[1,0],[0,1]]))


# [M-12] -----------------------------------------------------------------------------------------------------------------------
# Number of closed islands — islands completely surrounded by water (0=land, 1=water).
# Input:  [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
# Output: 2

def closedIslands(grid):
    pass

# print(closedIslands([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))


# ----- MATRIX MANIPULATION (8 problems) --------------------------------------------------------------------------------------

# [M-13] -----------------------------------------------------------------------------------------------------------------------
# Rotate image — rotate n×n matrix 90 degrees clockwise in-place.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotateImage(matrix):
    pass

# print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))


# [M-14] -----------------------------------------------------------------------------------------------------------------------
# Spiral matrix II — generate n×n matrix filled with 1 to n² in spiral order.
# Input:  n=3  →  Output: [[1,2,3],[8,9,4],[7,6,5]]

def generateSpiral(n):
    pass

# print(generateSpiral(3))


# [M-15] -----------------------------------------------------------------------------------------------------------------------
# Game of life — apply Conway's Game of Life rules for one generation in-place.
# Rules: live cell with 2-3 live neighbours survives; dead cell with 3 live neighbours becomes alive.
# Input:  [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

def gameOfLife(board):
    pass

# print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))


# [M-16] -----------------------------------------------------------------------------------------------------------------------
# Rotate matrix 180 degrees in-place.
# Input:  [[1,2,3],[4,5,6],[7,8,9]]  →  Output: [[9,8,7],[6,5,4],[3,2,1]]

def rotate180(matrix):
    pass

# print(rotate180([[1,2,3],[4,5,6],[7,8,9]]))


# [M-17] -----------------------------------------------------------------------------------------------------------------------
# Diagonal sort — sort each diagonal (top-left to bottom-right) independently.
# Input:  [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

def diagonalSort(matrix):
    pass

# print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))


# [M-18] -----------------------------------------------------------------------------------------------------------------------
# Lucky numbers in a matrix — elements that are min of their row and max of their column.
# Input:  [[3,7,8],[9,11,13],[15,16,17]]  →  Output: [15]

def luckyNumbers(matrix):
    pass

# print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))


# [M-19] -----------------------------------------------------------------------------------------------------------------------
# Shift 2D grid — shift all elements right by k positions (wrap around).
# Input:  grid=[[1,2,3],[4,5,6],[7,8,9]], k=1  →  Output: [[9,1,2],[3,4,5],[6,7,8]]

def shiftGrid(grid, k):
    pass

# print(shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))


# [M-20] -----------------------------------------------------------------------------------------------------------------------
# Matrix block sum — for each cell, sum all cells within distance k.
# Input:  mat=[[1,2,3],[4,5,6],[7,8,9]], k=1  →  Output: [[12,21,16],[27,45,33],[24,39,28]]

def matrixBlockSum(mat, k):
    pass

# print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))


# ----- DP ON MATRIX (9 problems) ---------------------------------------------------------------------------------------------

# [M-21] -----------------------------------------------------------------------------------------------------------------------
# Unique paths — how many distinct paths from top-left to bottom-right (only right or down)?
# Input:  m=3, n=7  →  Output: 28

def uniquePaths(m, n):
    pass

# print(uniquePaths(3, 7))


# [M-22] -----------------------------------------------------------------------------------------------------------------------
# Unique paths II — same as above but with obstacles (1=obstacle, 0=free).
# Input:  [[0,0,0],[0,1,0],[0,0,0]]  →  Output: 2

def uniquePathsII(obstacleGrid):
    pass

# print(uniquePathsII([[0,0,0],[0,1,0],[0,0,0]]))


# [M-23] -----------------------------------------------------------------------------------------------------------------------
# Minimum path sum — find path from top-left to bottom-right minimising sum (only right/down).
# Input:  [[1,3,1],[1,5,1],[4,2,1]]  →  Output: 7  (1→3→1→1→1)

def minPathSum(grid):
    pass

# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


# [M-24] -----------------------------------------------------------------------------------------------------------------------
# Triangle minimum path sum — find min path from top to bottom of triangle (adjacent elements only).
# Input:  [[2],[3,4],[6,5,7],[4,1,8,3]]  →  Output: 11  (2+3+5+1)

def minimumTotal(triangle):
    pass

# print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))


# [M-25] -----------------------------------------------------------------------------------------------------------------------
# Maximal square — find the largest square of 1s in a binary matrix.
# Input:  [["1","0","1"],["1","1","1"],["1","1","1"]]  →  Output: 4  (2×2 square)

def maximalSquare(matrix):
    pass

# print(maximalSquare([["1","0","1"],["1","1","1"],["1","1","1"]]))


# [M-26] -----------------------------------------------------------------------------------------------------------------------
# Count square submatrices with all ones.
# Input:  [[0,1,1,1],[1,1,1,1],[0,1,1,1]]  →  Output: 15

def countSquares(matrix):
    pass

# print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))


# [M-27] -----------------------------------------------------------------------------------------------------------------------
# Number of paths in a grid with exactly k coins (coins collected along path).
# Input:  grid=[[0,1,2],[3,1,0],[2,1,0]], k=3  →  Output: 2

def numberOfPaths(grid, k):
    pass

# print(numberOfPaths([[0,1,2],[3,1,0],[2,1,0]], 3))


# [M-28] -----------------------------------------------------------------------------------------------------------------------
# Minimum falling path sum — choose one element per row, adjacent to previous row's choice.
# Input:  [[2,1,3],[6,5,4],[7,8,9]]  →  Output: 13  (1+4+8... wait, 1+5+7=13)

def minFallingPathSum(matrix):
    pass

# print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))


# [M-29] -----------------------------------------------------------------------------------------------------------------------
# Out of boundary paths — count paths that move a ball out of m×n grid in maxMove moves.
# Input:  m=2, n=2, maxMove=2, startRow=0, startCol=0  →  Output: 6

def findPaths(m, n, maxMove, startRow, startCol):
    pass

# print(findPaths(2, 2, 2, 0, 0))


# ----- PREFIX SUM ON MATRIX (3 problems) -------------------------------------------------------------------------------------

# [M-30] -----------------------------------------------------------------------------------------------------------------------
# Range sum query 2D — answer multiple sum queries on a static matrix.
# sumRegion(row1, col1, row2, col2) returns sum of rectangle.

class NumMatrix:
    def __init__(self, matrix):
        pass
    def sumRegion(self, row1, col1, row2, col2):
        pass

# nm = NumMatrix([[3,0,1,4],[5,6,3,2],[1,2,0,1],[4,1,0,1]])
# print(nm.sumRegion(2,1,4,3))


# [M-31] -----------------------------------------------------------------------------------------------------------------------
# Count submatrices with all ones — count rectangles formed entirely of 1s.
# Input:  [[1,0,1],[1,1,0],[1,1,0]]  →  Output: 7

def numSubmat(mat):
    pass

# print(numSubmat([[1,0,1],[1,1,0],[1,1,0]]))


# [M-32] -----------------------------------------------------------------------------------------------------------------------
# Maximum sum rectangle in a 2D matrix.
# Input:  [[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]  →  Output: 29

def maxSumRectangle(matrix):
    pass

# print(maxSumRectangle([[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]))


# ----- BINARY SEARCH ON MATRIX (2 problems) ----------------------------------------------------------------------------------

# [M-33] -----------------------------------------------------------------------------------------------------------------------
# Search in a 2D matrix II — each row and column is sorted (not as strict as E-03).
# Input:  matrix=[[1,4,7],[2,5,8],[3,6,9]], target=5  →  Output: True

def searchMatrixII(matrix, target):
    pass

# print(searchMatrixII([[1,4,7],[2,5,8],[3,6,9]], 5))


# [M-34] -----------------------------------------------------------------------------------------------------------------------
# Kth smallest element in a sorted matrix (rows and cols both sorted).
# Input:  matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8  →  Output: 13

def kthSmallestMatrix(matrix, k):
    pass

# print(kthSmallestMatrix([[1,5,9],[10,11,13],[12,13,15]], 8))


# =============================================================================================================================
# HARD (12 problems) — Advanced DFS, DP, complex manipulations
# =============================================================================================================================

# [H-01] -----------------------------------------------------------------------------------------------------------------------
# Word search II — find all words from a list that exist in the board (Trie + DFS).
# Input:  board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#         words=["oath","pea","eat","rain"]  →  Output: ["eat","oath"]

def findWords(board, words):
    pass

# print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))


# [H-02] -----------------------------------------------------------------------------------------------------------------------
# Maximal rectangle — largest rectangle containing only 1s in binary matrix.
# Input:  [["1","0","1","0"],["1","0","1","1"],["1","1","1","1"],["1","0","0","1"]]
# Output: 6

def maximalRectangle(matrix):
    pass

# print(maximalRectangle([["1","0","1","0"],["1","0","1","1"],["1","1","1","1"],["1","0","0","1"]]))


# [H-03] -----------------------------------------------------------------------------------------------------------------------
# Dungeon game — find minimum initial health to rescue the princess (bottom-right to top-left DP).
# Input:  [[-2,-3,3],[-5,-10,1],[10,30,-5]]  →  Output: 7

def calculateMinimumHP(dungeon):
    pass

# print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))


# [H-04] -----------------------------------------------------------------------------------------------------------------------
# Cherry pickup — collect maximum cherries going from (0,0) to (n-1,n-1) and back.
# Input:  [[0,1,-1],[1,0,-1],[1,1,1]]  →  Output: 5

def cherryPickup(grid):
    pass

# print(cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))


# [H-05] -----------------------------------------------------------------------------------------------------------------------
# Cherry pickup II — two robots start from top row, collect max cherries.
# Input:  [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]  →  Output: 24

def cherryPickupII(grid):
    pass

# print(cherryPickupII([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))


# [H-06] -----------------------------------------------------------------------------------------------------------------------
# Count submatrices with sum equal to target.
# Input:  matrix=[[0,1,0],[1,1,1],[0,1,0]], target=0  →  Output: 4

def numSubmatrixSumTarget(matrix, target):
    pass

# print(numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))


# [H-07] -----------------------------------------------------------------------------------------------------------------------
# Largest plus sign — find the largest k such that there's a plus sign of order k.
# Input:  n=5, mines=[[4,2]]  →  Output: 2

def orderOfLargestPlusSign(n, mines):
    pass

# print(orderOfLargestPlusSign(5, [[4,2]]))


# [H-08] -----------------------------------------------------------------------------------------------------------------------
# Number of paths with k coins — count paths from (0,0) to (m-1,n-1) collecting exactly k coins.
# Input:  grid=[[0,1,2],[3,1,0],[2,1,0]], k=5  →  Output: 3

def numberOfPathsKCoins(grid, k):
    pass

# print(numberOfPathsKCoins([[0,1,2],[3,1,0],[2,1,0]], 5))


# [H-09] -----------------------------------------------------------------------------------------------------------------------
# Minimum cost to cut a grid — minimum cost to separate grid into 1×1 pieces with horizontal/vertical cuts.
# Input:  m=2, n=2, horizontalCuts=[1], verticalCuts=[1]  →  Output: 4

def minimumCostCutGrid(m, n, horizontalCuts, verticalCuts):
    pass


# [H-10] -----------------------------------------------------------------------------------------------------------------------
# Strange printer II — determine if a sequence of rectangle paint operations is valid.
# Input:  targetGrid=[[1,1,1],[3,3,2],[3,3,2]]  →  Output: True

def isPrintable(targetGrid):
    pass

# print(isPrintable([[1,1,1],[3,3,2],[3,3,2]]))


# [H-11] -----------------------------------------------------------------------------------------------------------------------
# Swim in rising water — find minimum time to travel from (0,0) to (n-1,n-1), can only move when water rises.
# Input:  [[0,2],[1,3]]  →  Output: 3

def swimInWater(grid):
    pass

# print(swimInWater([[0,2],[1,3]]))


# [H-12] -----------------------------------------------------------------------------------------------------------------------
# Cut off trees for golf event — cut trees in ascending height order, find total BFS steps.
# Input:  [[1,2,3],[0,0,4],[7,6,5]]  →  Output: 6

def cutOffTree(forest):
    pass

# print(cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
