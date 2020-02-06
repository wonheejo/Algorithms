
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
"""

# Problem 2775: Apartments women's society
import sys

x = int(input())
floor = []
number = []
cond = [[0] *14 for i in range(14)]
for i in range(x):
    floor.append(list(map(int, sys.stdin.readline().split())))
    number.append(list(map(int, sys.stdin.readline().split())))

print(floor)
print(number)
sum = 0

for i in range(14):
    for j in range(1, 15):
        sum = (j*(j+1))//2
        cond.append(sum)

def recur2(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return(recur2(a-1, b-1)+recur2(a-2, b-2))

recur2(2, 2)