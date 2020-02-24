
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
"""
