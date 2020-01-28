import time, datetime
# January 25th 2020
# Problem 2798: Black Jack

"""
def sum_array(numbers, x, y):
    sum = []
    max = 0
    for i in range(x):
        for j in range(i+1, x):
            for k in range(j+1, x):
                sum.append(numbers[i] + numbers[j] + numbers[k])

    for i in range(len(sum)):
        if sum[i] <= y:
            if sum[i] > max:
                max = sum[i]
    print(max)


x, y = map(int, input().split())
numbers = list(map(int, input().split()))

sum_array(numbers, x, y)


# Problem 2231: Find its smallest constructor

def smallest(x):

    temp_list = []
    temp_num = []
    min = 1000000
    if x < 55:
        for i in range(0, 54):
            temp_num.append(i)
            temp_list.append(i + sum(map(int, str(i))))
        print(temp_list)
        for i in range(len(temp_list)):
            if temp_list[i] == x and temp_list[i] < min:
                min = temp_num[i]

        if min != 1000000:
            print(min)
        else:
            print(0)

    else:
        small = x - 54
        for i in range(small, x):
            temp_num.append(i)
            temp_list.append(i + sum(map(int, str(i))))

        print(temp_list)
        for i in range(len(temp_list)):
            if temp_list[i] == x and temp_list[i] < min:
                min = temp_num[i]

        if min != 1000000:
            print(min)
        else:
            print(0)

x = int(input())
smallest(x)

# January 26th 2020
# Problem 7568: Comparing weight and height of all
total = int(input())
total_list = []
for i in range(total):
    total_list.append(input().split())

def check_size(total_list, total):
    ranked_list = []

    for i in range(total):
        rank = 1
        for j in range(total):
            if total_list[i][0] < total_list[j][0] and total_list[i][1] < total_list[j][1]:
                rank += 1

        ranked_list.append(rank)

    for i in ranked_list:
        print(i, end=' ')

check_size(total_list, total)


# Problem 1018: Remaking Chessboard
# INCOMPLETE(will do later)
x, y = map(int, input().split())
z = []

def splits(word):
    return [c for c in word]

for i in range(int(x)):
    z.append(splits(input()))

b = []
for i in range(x):
    print(z[i])

for i in range(x-7):
    print('I: {} | {}'.format(i, z[i]))
    for j in range(y-7):
        count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                print('I: ', z[i], j, k, l, z[k][l])
"""

# Problem 1436: End of the world number 666
# Incomplete(will do later)
x = int(input())


def strangenum(e, g, h):
    r = x % 19
    t = x / 19

    if r < 6:
        x = str(int(t)) + str(r - 1)
    elif r < 16:
        # Need extra code here
        x = str(int(t)) + str(666) + str(5)
    elif r < 19:
        x = str(r) + str(666)

    return x

for i in range(x):
    a = i
    b = i%19
    c = i/19
    print('input: {}, y: {}, z: {}, num: {}'.format(a, b, int(c)), strangenum(a, b, c))




