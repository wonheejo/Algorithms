
# February 16th 2020
# Problem 10872: Factorial
"""
x = int(input())

def recursion(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*recursion(x-1)

print(recursion(x))


# Problem 10870: Fibonacci
x = int(input())

def fibonacci(x):
    if x == 0 :
        return 0
    elif x <=2 :
        return 1
    else:
        return fibonacci(x-2)+fibonacci(x-1)

print(fibonacci(x))


# Febuary 18th 2020
# Problem 2447: Star patterns using Recursion
import sys, time
x = int(input())

def draw_star(i, j):
    while(i!=0):
        if (i%3==1) and (j%3==1):
            sys.stdout.write(' ')
            return None

        i = i//3
        j = j//3
    sys.stdout.write('*')

start = time.time()
for i in range(x):
    for j in range(x):
        draw_star(i, j)
    sys.stdout.write('\n')
finish = time.time()
print(finish-start)


for i in range(x):
    print('{} // {} : {}        {} % {} : {}'. format(i, 3, i//3, i//3, 3, (i//3)%3))


# Problem 11729: Hanoi tower using recursion
import time
x = int(input())

def hanoi_tower(x, start, destination, aux):

    if x == 1:
        print(start, destination)
        return
    hanoi_tower(x-1, start, aux, destination)
    print(start, destination)
    hanoi_tower(x-1, aux, destination, start)

print((2**x)-1)
hanoi_tower(x, 1, 3, 2)
"""