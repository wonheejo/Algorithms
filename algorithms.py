import time
import timeit

import math

"""
print("\    /\ ")
print(" )  ( ') ")
print("(  /  ) ")
print(" \(__)| ")


# A+B problem

a, b= input().split()

def sum(a, b):
    return (int(a)-int(b))

print(sum(a, b))


# fibonacci algorithm problem

counter = 0
counter1 = 0

def fibo(a):
    global counter
    global counter1
    if a==0:
        counter += 1
        return 0
    elif a==1:
        counter1 += 1
        return 1
    else:
        return fibo(a-1) + fibo(a-2)

def mainfunc(b):
    global counter
    global counter1

    for i in range(b):
        counter = 0
        counter1 = 0
        a = int(input())
        # print(fibo(a), " called fib(0) ", counter, " called fib(1) ", counter1)
        fibo(a)
        print(counter, counter1)

num = int(input())
mainfunc(num)


# bridge problem


def sum4(a):
    sumglob = 0
    sum = 0
    n = len(a)
    for i in range(0, n):
        print("Value of i =", i)
        sum = max(sum, 0) + a[i]
        print("Value of current sum = ", sum, " Value of current a[i] =", a[i])
        sumglob = max(sum, sumglob)
        print("Value of current sumblog =", sumglob, "\n")
    return sumglob

a = [4, -3, 1, 2, -6, 5, 2, -1, 4, 2]
print(sum4(a))



2020. January. 6th

multiplication problem using sys.stdin.readline() and split()
import sys

num = int(input())

for i in range(0, num):
    line = list(map(int, sys.stdin.readline().split()))

    print(line[0] + line[1])



print number from 1 to input number
num = int(input())

for i in range(1, num+1):
    print(i)



print decrementation of numbers
num = int(input())

for i in range(num, 0, -1):
    print(i)


get input and print + of two inputs with beautifully looking phrases
import sys
num = int(input())

for i in range(1, num+1):
    #line = list(map(int, sys.stdin.readline().split()))
    x, y = input().split()
    print('Case #', i, ': ', int(x)+int(y), sep='')

more prettier than the previous A+B problem
import sys
num = int(input())

for i in range(1, num+1):
    line = list(map(int, sys.stdin.readline().split()))
    print('Case #', i, ': ', line[0], ' + ', line[1], ' = ', line[0]+line[1], sep='')


#print number of stars in staircase design depending on the input by user
num = int(input())

for x in range(1, num+1):

    for y in range(x):
        print('*', sep='', end='')
    print('\n', end='')



2020 January 7th

#print number of stairs but based on the right side of the maximum number of stars
num = int(input())

for x in range(1, num+1):
    for y in range(num, x, -1):
        print(' ', sep='', end='')
    for z in range(1, x+1):
        print('*', sep='', end='')
    print('\n', end='')


#Janurary 11th
Print numbers smaller than X in a given array N
import sys

x, y = input().split()

num = int(x)
comp = int(y)

array = list(map(int, sys.stdin.readline().split()))
array2 = []

for i in range(0, num):
    #print('i = ', i, ' array[i]: ', array[i])
    if (array[i] < comp):
        array2.append(array[i])

for x in range(0, len(array2)):
    print(array2[x], end=' ')


#Print the addition of two numbers until 0 0 has been input by user

while True:
    x, y = input().split()

    if (int(x) == 0 and int(y) == 0):
        break

    print(int(x) + int(y))

#Print addition of two numbers until EOF

import sys

while True:
    answer = sys.stdin.readline()
    if answer == '' or answer == '\n':
        break
    else:
        x, y = answer.split()

    print(int(x) + int(y))


#January 13th
#Problem 8958: OX quiz

from itertools import groupby


x = int(input())
a = []
b = []
strlist = []
intlist = []
count = 0

for i in range(x):
    a.append(input())

for i in range(x):
    b.append([(c, len(list(g))) for c, g in groupby(a[i])])

for i in range(x):
    strlist.append([k[0] for k in b[i]])
    intlist.append([k[1] for k in b[i]])

for i in range(x):
    total = 0
    for j in range(len(strlist[i])):
        if (strlist[i][j] == 'O'):
            count = ((intlist[i][j] + 1)*(intlist[i][j]))//2
            total = total + count
    print(total)


#Problem 4344: Am I higher than average?

x = int(input())
a = []
b = []
for i in range(x):
    a.append(input().split())

for i in range(x):
    b.append(a[i][0])

for i in range(x):
    total = 0
    count = 0
    for j in range(1, len(a[i])):
        total = int(a[i][j]) + total
    average = total/int(b[i])
    #print(average)
    for j in range(1, len(a[i])):
        if (int(a[i][j]) > average):
            count += 1
    #print(count)
    ratio = count/int(b[i])*100
    #print(round(ratio, 3))
    print('%.3f'%ratio, '%', sep='')


#Problem 15596: Define function that returns sum of N integers

def solve(a):
    temp = 0
    for i in range(len(a)):
        temp = (int(a[i])+1)*int(a[i])/2
    return temp

def solve2(a):
    ans = 0
    ans = sum(a)
    return ans

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solve2(b))


# January 14th 2020
# Problem 4673: Self number function

def selfnum():
    temp = 0
    a = list(range(1, 10000))
    b = []
    for i in range(1, 10000):
        temp = i + sum(map(int, str(i)))
        b.append(temp)

    len1 = len(list(set(a) - set(b)))
    final = list(set(a) - set(b))
    for i in range(len1):
        for j in range(i+1, len1):
            if(final[i] > final[j]):
                temp = final[i]
                final[i] = final[j]
                final[j] = temp

    for i in range(len1):
        print(final[i])


selfnum()


# Problem 1065: Find the numbers that achieve arithmatic sequences below a given number N
x = int(input())

def checknum(x):
    if (x < 100):
        print(x)
    else:
        result = 99
        for i in range(100, x+1):
            result += hancheck(i)

        print(result)

def hancheck(x):
    num2 = x%100
    num3 = num2%10
    num1 = (x-num2)/100
    num2 = (num2-num3)/10

    if (num3 - num2) == (num2 - num1):
        return 1
    else:
        return 0
checknum(x)


#Problem 11654: Get the Ascii code of a character that has been input

x = input()
print(ord(x))

#Problem 11720: Print the addition of given number

x = int(input())
y = input()
temp = 0
sum = 0
num = [c for c in y]

for i in range(x):
    temp = num[i]
    sum += int(temp)

print(sum)

#Problem 10809: Finding the Alphabet

word = input()
check = [c for c in word]
final = [-1] * 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(26):
    for j in range(len(check)):
        if (check[j] == alphabet[i]) and (final[i] == -1):
            final.pop(i)
            final.insert(i, j)

for i in range(26):
    print(final[i], end=' ')


#Problem 2675: String Repetition

num = int(input())
first = []
second = []
third = []

for i in range(num):
    first.append(input())
    second.append([c for c in first[i]])
    for j in range(1):
        third.append(second[i][0])

for i in range(num):
    for j in range(2, len(second[i])):
        for k in range(int(third[i])):
            print(second[i][j], end='')
    print('')


# January 18th 2020
# Problem 1157: Print most used alphabet

x = input()

def mostcount(str):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    check = [0] *26
    alpha = []
    max = -1
    count = 0
    for c in str:
        alpha.append(c)

    # Count the number of appearance of each letters into the check list
    for i in range(len(alpha)):
        for j in range(26):
            if alpha[i].casefold() == alphabet[j].casefold():
                check[j] = check[j] + 1

    # Look for highest number count in check list
    for i in range(26):
        if check[i] > max:
            max = check[i]
            store = alphabet[i]

    # Check for duplicate highest number
    for i in range(26):
        if check[i] == max:
            for j in range(i+1, 26):
                if check[i] == check[j]:
                    count +=1
                    #print(alphabet[i], ':', check[i], alphabet[j], ':', check[j])

    if count > 0:
        print('?')
    else:
        print(store)

mostcount(x)
# Test cases:
# HelLoOTherE
# Mississipi
"""

# Problem 1152: Count number of words
from nltk import tokenize

x = input()

tokenize.sent_tokenize(x)
