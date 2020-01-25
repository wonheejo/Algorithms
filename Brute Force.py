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
"""
