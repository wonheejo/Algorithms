# April 16th 2020
# Problem 2748: Fibonacci no.2 Using dynamic programming approach
"""
import sys, time
n = int(sys.stdin.readline())
fibseq = [0, 1]

start = time.time()

def fib(n):

    if n < len(fibseq):
        return fibseq[n]
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    fibseq.append(result)
    return result

print(fib(n))
#print(fibseq)
finished = time.time()
print(finished-start)
"""

# Problem 1003: Fibonacci no.3 Get number of 1s and 0s called

import sys

n = int(sys.stdin.readline())
test = []

for i in range(n):
    test.append(int(sys.stdin.readline()))

def fib(n):
    global fib0, fib1

    if n < len(fibseq):
        if n == 0:
            fib0, fib1 = 1, 0
        if n == 1:
            fib0, fib1 = 0, 1

        return fibseq[n]
    else:
        result = fib(n-1) + fib(n-2)
        result2 = fib(n-2) + fib(n-3)

    fibseq.append(result)

    fib1 = result
    fib0 = result2
    return result

for i in test:
    fibseq = [0, 1]
    fib0 = 0
    fib1 = 0
    fib(i)
    print(fib0, fib1)


