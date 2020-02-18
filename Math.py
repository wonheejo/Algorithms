
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


# Febuary 8th 2020
# Problem 1011: Fly me to alpha centauri
# Tried to look for the warp count using iterative method but it didnt succeed....
import sys, math

x = int(input())
coor = []
warpdist = []
for i in range(x):
    coor.append(list(map(int, sys.stdin.readline().split())))

print(coor)

for i in range(x):
    z = coor[i][1]
    y = coor[i][0]
    dist = z-y
    print(math.ceil((z-y)/2))
    k = 1
    warp = 0
    print('Current distance: {}' .format(dist))
    while dist > 0:
        if dist > math.ceil((z-y)//2):
            print('if comp')
            warp += 1
            dist -= k
            print('warps done: {}, warped length: {}, current distance: {}'.format(warp, k, dist))

            if dist > math.ceil(((z-y)/2)) and dist-(k+1) >= (k)*(k+1)/2:
                k += 1
            elif k >= 2 and (dist <= 5):
                k -= 1
            else:
                k = k
            print('next jump length: {}' .format(k))
        else:
            print('else comp')
            warp += 1
            dist -= k
            print('warps done: {}, warped length: {}, current distance: {}'.format(warp, k, dist))
            if dist <= 2:
                k = 1
            elif dist > 2 and k <= 2:
                k = k
            else:
                k -= 1

            print('next jump length: {}' .format(k))

    warpdist.append(warp)


import sys, math

x = int(input())
coor = []
warpdist = []
for i in range(x):
    coor.append(list(map(int, sys.stdin.readline().split())))

for i in range(x):
    y = coor[i][1]
    z = coor[i][0]
    dist = y-z
    n = 1
    warp = 1
    while True:
        if dist >= (n**2)-(n+1) and dist <= (n**2)+n:
            if dist <= (n**2):
                warpdist.append(warp)
                break
            else:
                warp += 1
                warpdist.append(warp)
                break
        warp += 2
        n += 1

for i in range(x):
    print(warpdist[i])


# Problem 1978: Prime numbers
import sys, math
x = int(input())

prime = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(x):
    if prime[i] == 2:
        count += 1
    elif (prime[i] > 2) and (prime[i]%2 != 0):
        #print(prime[i])
        tick = 0
        for j in range(1, prime[i]+1):
            check = prime[i]%j
            #print('{} % {} = {}' .format(prime[i], j, check))
            if check == 0:
                tick += 1
            if tick > 2:
                break
        if tick <= 2:
            count += 1
            #print('{} is a prime so incremented, tick count: {}' .format(prime[i], tick))

print(count)


# Problem 2581: Finding Prime numbers 2

x = int(input())
y = int(input())

z = y-x

prime = []
count = 0
min = 10001

for i in range(x, y+1):
    if i == 2:
        prime.append(i)
    elif(i > 2) and (i%2 != 0):
        tick = 0
        for j in range(1, i+1):
            check = i%j
            if check == 0:
                tick += 1
            if tick > 2:
                break
        if tick <= 2:
            prime.append(i)
    if i in prime:
        #print('{} is in prime' .format(i))
        if i < min:
            min = i

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min)


# Febuary 9th 2020
# Problem 1929: Find and print prime numbers
import sys, math, time
x, y = sys.stdin.readline().split()
x = int(x)
y = int(y)
prime = set()

start = time.time()

for i in range(2, y + 1):
    prime.add(i)


for i in range(2, int(math.sqrt(y)+1)):
    if i in prime:
        for j in range(i*2, y+2, i):
            if j in prime:
                prime.remove(j)

finish = time.time()

for i in prime:
    if i >= x:
        print(i)
print(finish - start)


# Problem 4989: Finding primes Bertrands postulate

import sys, math, time
inputs = []
while True:
    temp = int(input())
    if temp == 0:
        break
    else:
        inputs.append(temp)

prime = set()
start = time.time()


for i in range(2, 246914):
    prime.add(i)

for i in range(2, int(math.sqrt(246914)+1)):
    if i in prime:
        for j in range(i*2, 246918, i):
            if j in prime:
                prime.remove(j)

for j in inputs:
    upper = j*2
    tempset = set()
    for i in range(j+1, upper+1):
        tempset.add(i)

    print(len(tempset.intersection(prime)))


finish = time.time()

print(finish - start)


# Problem 9020: Goldbach conjecture
import sys, time, math

x = int(input())
even = []

for i in range(x):
    even.append(int(sys.stdin.readline()))

# Uses Eratosthanes's sieve to find all the primes upto 10000 just once
start = time.time()
prime = set()
for i in range(2, 10000):
    prime.add(i)

for i in range(2, int(math.sqrt(10000)+1)):
    if i in prime:
        for j in range(i*2, 10002, i):
            if j in prime:
                prime.remove(j)
end = time.time()

# Using the primes found just once, the loop below searches through the set of primes and finds the correct pairs
start2 = time.time()
for i in even:
    max = 0
    tempset = []

    # Looking through the set for the i-th prime and adds it into a list
    for k in prime:
        if (k + (i-k) == i) and (k > max) and (i-k) in prime and (k <= (i-k)):
            max = k
    print(max, i-max)


finish = time.time()

print('time for finding primes:', end - start)
print('time for finding the sums:', finish - start2)


# February 15th 2020
# Problem 1085: Shortest path to edge of rectangle
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
print(x, y, w, h)

distx1 = x-0
disty1 = y-0
distx2 = w-x
disty2 = h-y

# print('dist x-0: {}, dist y-0: {}, dist w-x: {}, dist h-y: {}' .format(distx1, disty1, distx2, disty2))

if distx1 <= distx2:
    temp1 = distx1
else:
    temp1 = distx2

if disty1 <= disty2:
    temp2 = disty1
else:
    temp2 = disty2

if temp1 <= temp2:
    print(temp1)
else:
    print(temp2)


# Problem 3009: Finish the rectangle
import sys, math
coor = []
for i in range(3):
    coor.append(list(map(int, sys.stdin.readline().split())))

for i in range(3):
    for j in range(i+1, 3):
        if coor[i][0] == coor[j][0]:
            temp1 = coor[i]
            temp2 = coor[j]

for i in range(3):
    if coor[i] != temp1 and coor[i] != temp2:
        temp3 = coor[i]
height = abs(temp1[1] - temp2[1])

if temp3[1] > height:
    last = temp3[1] - height
else:
    last = temp3[1] + height

print(temp3[0], last)


# Problem 4153: Right angled triangle
import sys
tri = []

while True:
    temp = list(map(int, sys.stdin.readline().split()))

    if temp[0]==0:
        break
    else:
        tri.append(temp)

lens = len(tri)

for i in range(lens):
    x = tri[i][0]
    y = tri[i][1]
    z = tri[i][2]
    if x*x == y*y + z*z:
        print('right')
    elif (y*y == x*x + z*z):
        print('right')
    elif (z*z == x*x + y*y):
        print('right')
    else:
        print('wrong')


 # Problem 3053:
import math
x = int(input())

print('{:.6f}' .format(math.pi*(x*x)))
print('{:.6f}' .format(x*x*2))


# Problem 1002: Turret
import sys, math
x = int(input())
coor = []
for i in range(x):
    coor.append(list(map(int, sys.stdin.readline().split())))

for i in range(x):
    x1 = coor[i][0]
    y1 = coor[i][1]
    r1 = coor[i][2]
    x2 = coor[i][3]
    y2 = coor[i][4]
    r2 = coor[i][5]
    count = 0
    minr = 0
    maxr = 0
    if r1 != r2 and r1 < r2:
        minr = r1
        maxr = r2
    elif r1 != r2 and r1 > r2:
        minr = r2
        maxr = r1

    dist1 = math.sqrt(abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2))
    dist2 = r1 + r2
    if dist1 == dist2: # When distance between two points is equal to r1+r2
        count = 1
    elif dist1 > dist2: # When distance between two point is larger than r1+r2
        count = 0
    else: # When the distance between two point is smaller than r1+r2
        if (dist1+minr) < maxr:
            count = 0
        elif (dist1+minr) == maxr and r1 != r2:
            count = 1
        elif dist1 == 0 and r1 == r2:
            count = -1
        else:
            count = 2
    print(count)
"""