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


