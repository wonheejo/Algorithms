
# Samsung Practice Coding section

# Basic 1

""""
for i in range(1, 20):
    for j in range(1, 20, 2):
        if j != 19:
            print(i, '*', j, '=', i*j, '/', i, '*', j+1, '=', i*(j+1))
        else:
            print(i, '*', j, '=', i*j)

"""
# Basic 2
"""
num = int(input())
saved = []

for i in range(1, num+1):
    dia = 2*i - 1
    saved.append(dia)
    for k in range(num-i, 0, -1):
        print(' ', end='')

    for j in range(dia):
        print('*', end='')
    print('')

for i in range(len(saved)-1, 0, -1):
    next = saved[i-1]
    for k in range(num-i, 0, -1):
        print(' ', end='')
    for j in range(next):
        print('*', end='')
    print('')
"""

# Basic 3
"""
import sys

num = int(input())
my = list(map(int, sys.stdin.readline().split()))
min = 1e+9 # works with using my[0] but i'm not sure why it doesnt work with setting it to a 1e+9 specific value
count = 0

for i in range(0, num):
    if my[i] < min:
        min = my[i]

for i in range(num):
    if my[i] == min:
        #print(my[i], i)
        count += 1

print(min, count)
"""

# Basic 4
"""
import sys

num = int(input())
my = list(map(int, sys.stdin.readline().split()))
max = my[0]

for i in range(0, num):
    if my[i] > max:
        max = my[i]
        index = i
    elif my[i] == max:
        index = i

my.pop(index)

max2 = my[0]
for i in range(0, num-1):
    if my[i] > max2:
        max2 = my[i]

print(max, max2)
"""

# Basic 5
"""
str1 = input()
str2 = input()

index = str1.find(str2)

print(index)
"""

# Basic 6
"""
line, num = input().split()
num = int(num)
orders = []
line_len = len(line)
for i in range(num):
    orders.append(int(input()))

for i in range(num):
    if orders[i] == 1:
        temp = line[0]
        line = line[1:]+temp
        print(line)
    elif orders[i] == 2:
        temp = line[-1]
        line = temp+line[:(line_len)-1]
        print(line)
    elif orders[i] == 3:
        line = line[::-1]
        print(line)
"""

# Basic 7
"""
x, y = tuple(map(int, input().split()))

used = [[0 for i in range(y)] for _ in range(x)]
count = 1

def fill_space(row, col):
    global count

    while col >= 0 and row < x:
        used[row][col] = count
        #print('count: {}, row: {}, col: {}'.format(count, row, col))

        row += 1
        col -= 1
        count += 1

for col in range(y):
    #print('col: ', col)
    fill_space(0, col)

for row in range(1, x):
    #print('row: ', row)
    fill_space(row, y-1)

for i in range(x):
    for j in range(y):
        print(used[i][j], end=' ')
    print()
"""

# Basic 8 (Incomplete)
"""
x, y = tuple(map(int, input().split()))
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']

used = [[0 for i in range(y)] for j in range(x)]
count = 0



for i in range(x):
    for j in range(y):
        print(used[i][j], end=' ')
    print()
"""

# Basic 9
"""
x = input()
y = input()

first = []
second = []
check_count = 0

def check_same(x, y):
    global check_count

    for i in range(len(x)):
        first.append(x[i])

    for j in range(len(y)):
        second.append(y[j])

    first_sorted = sorted(first)
    second_sorted = sorted(second)

    for i in range(len(x)):
        if first_sorted[i] == second_sorted[i]:
            check_count += 1

    return check_count

if len(x) != len(y):
    print('No')
else:
    if check_same(x, y) == len(x):
        print('Yes')
    else:
        print('No')
"""

# Basic 10
"""
x = int(input())
y = list(map(int, input().split()))

sorted_list = []
final_list = [0 for _ in range(x)]

check_index = [
    (number, i) for i, number in enumerate(y)
]

sorted_list = sorted(check_index)

for i, (first, second) in enumerate(sorted_list):

    final_list[second] = i + 1

for i in range(x):
    print(final_list[i], end=' ')

"""