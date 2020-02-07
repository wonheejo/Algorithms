
# Febuary 6th 2020
# Problem 1712: Break Even Point
"""
import sys

a, b, c = map(int, sys.stdin.readline().split())

if b >= c:
    print(-1)
else:
    print((a // (c - b)) + 1)


# Problem 2839: Sugar Factory
a = int(input())

b = 0
temp = 0
limit = int(a/3)+1
ans = []

for i in range(limit):
    sum = []
    c = 0
    for j in range(limit):
        sum.append(b+c)
        c += 3
        if sum[j] == a:
            #print('{} = 5*{} + 3*{}' .format(a, i, j))
            temp = (i) + (j)
            ans.append(temp)
            break
    b += 5
if len(ans) == 0:
    print(-1)
else:
    print(ans[-1])


# Problem 2292: Beehive problem
x = int(input())
temp = 1

if x == 1:
    print(1)
elif(x<=7):
    print(2)
else:
    for i in range(x):
        temp += 6*i
        #print(temp, i+1)
        if x<=temp:
            print(i+1)
            break


# Problem 1193: Fractional Number

x = int(input())

s = 1
y = 2

while x>s:
    s += y
    y += 1
    #print(x, s, y)

odd = y%2
N = s - x + 1
D = y - s + x - 1
if odd == 0:
    print('{}/{}' .format(N, y-N))
else:
    print('{}/{}' .format(D, y-D))


# Problem 2869: Snail wants to go up
import sys
import math

max, loss, total = map(int, sys.stdin.readline().split())

days = (total-loss) / (max-loss)
days = math.ceil(days)
print(days)


# Problem 10250: ACM hotel
import sys
x = int(input())
hotel = []
floor = []
roomnumber = []
for i in range(x):
    hotel.append(list(map(int, sys.stdin.readline().split())))

for i in range(x):
    room = 0
    for j in range(hotel[i][1]):
        for k in range(hotel[i][0]):
            room += 1
            if room == hotel[i][2]:
                floor.append(k+1)
                roomnumber.append(j+1)

for i in range(x):
    if roomnumber[i] < 10:
        print('{}0{}' .format(floor[i], roomnumber[i]))
    else:
        print('{}{}' .format(floor[i], roomnumber[i]))


# Febuary 7th 2020
# Problem 2775: Apartments women's society
import sys, math

x = int(input())
floor = []
number = []
for i in range(x):
    floor.append(int(sys.stdin.readline()))
    number.append(int(sys.stdin.readline()))

for i in range(x):
    integer = 1
    total = number[i]*(number[i]+1)
    #print('room number:', number[i], 'sum of total:', total)
    for j in range(floor[i]):
        #print('floor number:', floor[i])
        integer = (1/(j+2))*integer
        if j == 0:
            total = total
        else:
            total = total*(number[i]+(j+1))
        #print('sum:', total*integer)

    final = math.ceil(total*integer)
    print(final)

"""

# Problem 1011: Fly me to alpha centauri
import sys

x = int(input())
coor = []
warpdist = []
for i in range(x):
    coor.append(list(map(int, sys.stdin.readline().split())))
print(coor)

for i in range(x):
    k = 1
    warp = 0
    warpdist.append(coor[i][1] - coor[i][0]-2)


print(warpdist)

