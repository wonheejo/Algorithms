# April 16th 2020
# Problem 2748: Fibonacci no.2 Using dynamic programming approach

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
