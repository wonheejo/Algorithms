
"""
# Febuary 21th 2020
# Problem 15649: N and M
import sys
x, y = map(int, sys.stdin.readline().split())
nums = [0 for i in range(x+1)]
check = [0 for i in range(y)]

def shownum(index, x, y):
    if index == y:
        print(*check, end='')
        print()
        return
    for i in range(1, len(nums)):
        if nums[i] == 1:
            continue
        nums[i] = 1
        check[index] = i
        shownum(index+1, x, y)
        nums[i]  = 0

shownum(0, x, y)


# Problem 15650: N and M (2)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = [0 for i in range(x+1)]
check = [0 for i in range(y)]
duplicate = []

def shownum(index, x, y):
    if index == y:
        temp = sorted(check)
        if (temp not in duplicate):
            print(*temp)
            duplicate.append(temp[:])
        return

    for i in range(1, len(nums)):
        if nums[i] == 1:
            continue
        nums[i] =1
        check[index] = i
        shownum(index+1, x, y)
        nums[i] = 0

shownum(0, x, y)


# Problem 15651: N and M (3)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = [0 for i in range(x+1)]
check = [0 for i in range(y)]

def shownum(index, x, y):
    if index == y:
        print(*check)
        return

    for i in range(1, len(nums)):

        check[index] = i
        nums[i] = 1
        shownum(index+1, x, y)
        nums[i] = 0


shownum(0, x, y)


# Febuary 24th 2020
# Problem 15652: N and M (4)
import sys
x, y = map(int, sys.stdin.readline().split())

nums = [0 for i in range(x+1)]
check = [0 for i in range(y)]

def shownum(index, x, y):
    if index == y:
        print(*check)
        return

    for i in range(1, len(nums)):
        #print('inside for loop')
        #print('i:{}   check[index]: {}, index: {}, index-1: {}' .format(i, check[index-1], index, index-1))

        if index >= 1 and i >= check[index-1]:
            check[index] = i
        elif index == 0:
            check[index] = i
        else:
            continue

        #print('check: {}' .format(check))
        shownum(index+1, x, y)

shownum(0, x, y)


# Problem 15654: N and M (5)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
check = [0 for i in range(y)]
isused = [0 for i in range(x+1)]

def shownum(index, nums, x, y):
    if index == y:
        print(*check)
        return

    for i in range(x):
        if isused[i] == True:
            continue

        check[index] = nums[i]

        isused[i] = True
        shownum(index+1, nums, x, y)
        isused[i] = False

shownum(0, nums, x, y)


# Problem 15655: N and M (6)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
isused = [0 for i in range(x+1)]
check = [0 for i in range(y)]
duplicate = []

def shownum(index, nums, x, y):
    if index == y:
        temp = sorted(check)
        if temp not in duplicate:
            print(*temp)
            duplicate.append(temp[:])
        return

    for i in range(x):
        if isused[i] == True:
            continue
        check[index] = nums[i]
        isused[i] = True
        shownum(index+1, nums, x, y)
        isused[i] = False

shownum(0, nums, x, y)


# Problem 15656: N and M (7)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
check = [0 for i in range(y)]

def shownum(index, y):
    if index == y:
        print(*check)
        return

    for i in range(x):
        check[index] = nums[i]
        shownum(index+1, y)
shownum(0, y)


# Problem 15657: N and M (8)
import sys
x, y = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
check = [0 for i in range(y)]

def shownum(index, y):
    if index == y:
        print(*check)
        return

    for i in range(x):

        if index>=1 and nums[i] >= check[index-1]:
            check[index] = nums[i]
        elif index == 0:
            check[index] = nums[i]
        else:
            continue

        shownum(index+1, y)

shownum(0, y)


# Febuary 25th 2020
# Problem 9663: N-Queen Problem

import sys, time
x = int(sys.stdin.readline())
y = x-1 # Used for counting diagonals

start = time.time()
board = [[0 for i in range(x)] for j in range(x)]
row = [0 for i in range(x)]
diagrightB = [0 for i in range(x+y)]
diagleftT = [0 for i in range(x+y)]
count = 0

def solvequeen(x, board, col):
    global count
    if col == x:
        count += 1
        return

    for i in range(x):

        if 1 in board[i] or diagleftT[i-col+(x-1)] == 1 or diagrightB[i+col] == 1:
            continue

        board[i][col] = 1
        row[col] = 1
        diagrightB[i+col] = 1
        diagleftT[i-col+(x-1)] = 1

        solvequeen(x, board, col+1)

        board[i][col] = 0
        row[col] = 0
        diagrightB[i+col] = 0
        diagleftT[i-col+(x-1)] = 0

solvequeen(x, board, 0)
finish = time.time()
print(count)
print(finish-start)
"""

# Problem 2580: Sudoku
import sys, time
board = []

for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

start = time.time()

def find_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) # row, col

    return None

def valid(board, n, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == n and pos[1] != i:
            return False

    # Check col
    for i in range(len(board[0])):
        if board[i][pos[1]] == n and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == n and (i, j) != pos:
                return False

    return True

def solve_board(board):

    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for i in range(9):
        print(*board[i])


#print_board(board)
#print('')
solve_board(board)

finish = time.time()
print_board(board)

print('-')
print(finish-start)