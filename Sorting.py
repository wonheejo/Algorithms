import sys
# January 28th 2020
# Problem 2750: O(n^2) Sorting algorithm, Bubble sort
"""
x = int(input())
y = []
for i in range(x):
    y.append(int(input()))

temp = 0
for i in range(x):
    for j in range(i+1, x):
        if y[i] > y[j]:
            temp = y[i]
            y[i] = y[j]
            y[j] = temp

for i in range(x):
    print(y[i])


# Problem 2751: O(nlogn) Sorting algorithm, Merge sort
x = int(input())
y = []
for i in range(x):
    y.append(int(input()))

def merge_first(y):
    if len(y) <= 1:
        return y

    mid = len(y) // 2
    left = merge_first(y[:mid])
    right = merge_first(y[mid:])

    return merge_second(left, right, y)

def merge_second(left, right, c):

    l, r = 0, 0

    while(l < len(left)) and (r < len(right)):
        if(left[l] <= right[r]):
            c[l+r] = left[l]
            #c.insert(l+r, left[l])
            l += 1
        else:
            c[l+r] = right[r]
            #c.insert(l+r, right[r])
            r += 1

    for l in range(l, len(left)):
        c[l+r] = left[l]

    for r in range(r, len(right)):
        c[l+r] = right[r]

    return c


merge_first(y)

for i in range(x):
    print(y[i])


# Problem 10989: Counting Sort

x = int(sys.stdin.readline())
count = [0]*10001

for i in range(x):
    #temp = int(sys.stdin.readline())
    count[int(sys.stdin.readline())] += 1

for i in range(10001):
    for k in range(count[i]):
        print(i)
    
"""

# January 30th 2020
# Problem 2108: Statistic
# Incomplete

from collections import Counter
x = int(sys.stdin.readline())
y = []

for i in range(x):
    y.append(int(sys.stdin.readline()))

modes = Counter(y)
second= modes.most_common(1)[0][0]
dup = []
count = 0

y.sort()
for fir, i in enumerate(y):
    for sec, j in enumerate(y):
        if fir < sec and y[fir] == y[sec] and y[fir] not in dup:
            count += 1
            dup.append(y[fir])
print(dup)
# Print mean value of list
print(int(round(sum(y)/x, 0)))

# Print median value of list
# print(y)
# print('len(y)/2: {}, y[len(y)/2]: {}' .format(len(y)/2, y[int(len(y)/2)]))
print(y[int(len(y)//2)])
# print(sorted(y)[x // 2])

# Print second smallest mode value of list
if len(dup) > 2:
    print(dup[1])
elif len(dup) == 1:
    print(dup[0])
else:
    print(second)


if len(dup) > 2:
    print(dup[1])
elif len(dup) == 2:
    print(dup[-1])
elif (len(dup) == 1):
    print(dup[0])
elif len(dup) == 0 and len(y) == 1:
    print(y[0])
elif len(dup) == 0 and len(y) > 1:
    print(y[1])


# Print the difference between max and min of list
print((max(y) - min(y)))


"""
# Problem 1427
x = list(map(int, input()))

def merge_first(x):
    if len(x) <= 1:
        return x

    mid = len(x) // 2

    left = merge_first(x[:mid])
    right = merge_first(x[mid:])

    return merge_second(left, right, x)

def merge_second(left, right, c):
    l, r = 0, 0

    while (l<len(left)) and (r<len(right)):
        if (left[l] >= right[r]):
            c[l+r] = left[l]
            l += 1
        else:
            c[l+r] = right[r]
            r += 1

    for l in range(l, len(left)):
        c[l+r] = left[l]

    for r in range(r, len(right)):
        c[l+r] = right[r]

    return c

merge_first(x)

for i in range(len(x)):
    print(x[i], end='')


# Problem 11650: Sorting Coordinates
x = int(input())
y = []
for i in range(x):
    y.append(list(map(int, sys.stdin.readline().split())))

def merge(y):
    if len(y) <= 1:
        return y
    mid = len(y) // 2
    left = merge(y[:mid])
    right = merge(y[mid:])

    return merge_second(left, right, y)

def merge_second(left, right, c):
    l, r = 0, 0

    while(l<len(left)) and (r<len(right)):
        if left[l] <= right[r]:
            c[l+r] = left[l]
            l += 1
        else:
            c[l+r] = right[r]
            r += 1

    for l in range(l, len(left)):
        c[l+r] = left[l]

    for r in range(r, len(right)):
        c[l+r] = right[r]

    return c

merge(y)
for i in range(x):
    print(*y[i])


# Just some random code i thought i needed but the merge sort sorted the entire list even to the second variables.... 
dup = []
index = []
for fir, i in enumerate(y):
    for sec, j in enumerate(y):
        if fir < sec and y[fir][0] == y[sec][0] and y[fir][0] not in dup:
            dup.append(y[fir][0])
            index.append(fir)

print('dup:', dup)
print('index:', index)
print('count:', len(dup))

count1 = [0] * len(index)
to_change = []
for i in range(len(index)):
    temp = y[index[i]][0]
    for j in range(len(y)):
        if y[j][0] == temp:
            count1[i] += 1

print('count of each index:', count1)
for i in range(len(dup)):
    for j in range(index[i], index[i]+count1[i]):
        to_change.append(y[j][1])
    print(to_change)
    merge(to_change)
    print(to_change)
    del to_change[:]


# January 31th 2020
# Problem 11651: Sorting Coordinates 2(sort by y value)
import sys

x = int(input())
y = []
for i in range(x):
    y.append(list(map(int, sys.stdin.readline().split())))

# Used Python's built in sorting function
y3 = sorted(y, key=lambda k: [k[1], k[0]])

for i in range(x):
    print(*y3[i])



# Problem 1181: Sorting text into difference in length

import sys
x = int(sys.stdin.readline())
y = []
y_sorted = []
for i in range(x):
    y.append(sys.stdin.readline())

y_set = set(y)

for i in y_set:
    y_sorted.append(i)

y_sorted.sort()
y_sorted = sorted(y_sorted, key=len)


for i in range(len(y_sorted)):
    print(y_sorted[i], end='')


# Problem 10814: Sorting by age

import sys

x = int(sys.stdin.readline())
y = []
y1 = []
for i in range(x):
    y.append(sys.stdin.readline().split())

# Made my own function to use as a key which returns the first value of in the list of a list
def func(s):
    return int(s[0])
y1 = sorted(y, key=func)

for i, j in y1:
    print(i, j)

"""
