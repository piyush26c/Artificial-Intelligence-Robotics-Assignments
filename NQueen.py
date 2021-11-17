# -*- coding: utf-8 -*-
"""
Topic  : Constraint Satisfaction Problem (N-Queen Problem)
"""

# n decides size of board
n = 4

# a is a 2-D array to hold board and following code initializes a with zero
a = [[0 for x in range(n)] for y in range(n)]

# b is dictionary (like map) that stores key value pair. it is used to store row and safe column no for the same row.
b = {}

# To check in column
def isColumnSafe(r, c):
    while(r >= 0):
        if (a[r][c] == 1):
            return 0
        r = r - 1
    return 1

# To check in left diagonal
def isLeftDiagonalSafe(r, c):
    while(r >= 0 and c >= 0):
        if(a[r][c] == 1):
            return 0
        r = r - 1
        c = c - 1
    return 1

# To check in right diagonal
def isRightDiagonalSafe(r, c):
    while(r >= 0 and c < n):
        if(a[r][c] == 1):
            return 0
        r = r - 1
        c = c + 1
    return 1

# function to check given row and col position is safe or not.
# returns 0 if not safe else 1
def isSafe(row, col):
    if(isColumnSafe(row, col) == 0):
        return 0
    if(isLeftDiagonalSafe(row, col) == 0):
        return 0
    if(isRightDiagonalSafe(row, col) == 0):
        return 0
    return 1

# Recursive function to check row wise safe position for each queen(n).
def checkBoard(r, c):
    if(r >= n):
        return
    p = 0
    while(c < n):
        p = isSafe(r, c)
        if(p == 1):
            a[r][c] = 1
            b.update({r : c})
            break
        c = c + 1
    if(p == 1):
        checkBoard(r + 1, 0)   # Calling recursion for next row
    else:
        a[r - 1][b.get(r - 1)] = 0
        checkBoard(r - 1, int(b.get(r - 1)) + 1)   # Here actual backtracking happens for previous row

if __name__ == '__main__':
	checkBoard(0, 0)
	print("\n\nChess Board Grid: \n")
	for i in range(0, len(a)):
		for j in a[i]:
			print(j, end = " ")
		print("\n")

"""
Input - 1:
n = 4

Output - 1:

Chess Board Grid: 

0 1 0 0 

0 0 0 1 

1 0 0 0 

0 0 1 0 
"""