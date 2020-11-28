

# Leetcode problem 20. Valid Parenthesis
# Doesnt include the main class and functions, only the necessary code for the function in leetcode to work is written here!
"""
s = input()
checking = []


for i in range(len(s)):
    checking.append(s[i])

print(checking)

count = 0
index = 0
stack = []

while index < len(checking):

    print('Count is: {} and Index is at: {}'.format(count, index))
    print('Current checking[Index] to be added is: {}'.format(checking[index]))

    if count >= 1 and checking[index] == ']' and stack[count-1] == '[':
        print('Popped : {}'.format(stack[count - 1]))
        stack.pop(count-1)
        count -= 1
    elif count >= 1 and checking[index] == '}' and stack[count-1] == '{':
        print('Popped : {}'.format(stack[count - 1]))
        stack.pop(count-1)
        count -= 1
    elif count >= 1 and checking[index] == ')' and stack[count-1] == '(':
        print('Popped : {}'.format(stack[count - 1]))
        stack.pop(count-1)
        count -= 1
    else:
        stack.append(checking[index])
        print('Added {} to the stack.'.format(checking[index]))
        count += 1

    index += 1
    print('Current stack is: {}'.format(stack))
"""

# Leetcode problem 21.Merge two sorted lists



# Leetcode problem 26. Remove duplicates from a sorted list
"""
def removeDuplicates(self, nums: List[int]) -> int:
    # print(nums)

    duplicate = []

    listlen = len(nums)
    count = 0
    index = 0
    while index < listlen - 1:

        # print('Count = {}, Index = {}'.format(count, index))
        # print('List before action: {}'.format(nums))
        if index < listlen - 1 and nums[count] != nums[count + 1]:
            # print('Count incremented!')
            count += 1
        else:
            # print('Popped: {}'.format(count+1))
            nums.pop(count + 1)
        index += 1
        # print('List after action: {}'.format(nums))

    # print(nums)
    
"""

# Leetcode problem 27. Remove specified element from array
"""
def removeElement(self, nums: List[int], val: int) -> int:
    #print(nums)
    #print('To remove: ',val)
        
    listlen = len(nums)
    index = 0
    count = 0
    while index < listlen:
            
        #print('Count: {} and Index: {}'.format(count, index))
        #print('Current value to be compared: {}'.format(nums[count]))
        if nums[count] == val:
            #print('Popped {} !!'.format(nums[count]))
            nums.pop(count)
        else:
            count += 1
            
        index += 1
        #print(nums)

"""

# Leetcode problem 28. implement strStr(), aka. find index of matching substring in string
"""
def strStr(self, haystack: str, needle: str) -> int:
    print('Haystack: ',haystack)
    print('Needle', needle)
        
    if len(needle) == 0:
        return 0
    else:
        result = haystack.find(needle)

        if result != -1:
            return result
        else:
            return -1

"""

# Leetcode problem 55. Maximum subarray
"""
def maxSubArray(self, nums: List[int]) -> int:
    #print(nums)
        
    sum = 0
    sumglob = nums[0]
        
    if len(nums) == 1:
            return nums[0]
    else:
        for i in range(len(nums)):
            print('Index: {}, num: {}'.format(i, nums[i]))
            print('sum so far: {}'.format(sum))
            print('sumglob: {}'.format(sumglob))
                
            sum = max(sum, 0) + nums[i]
                
            sumglob = max(sum, sumglob)
                

        print(sumglob)
        return sumglob

"""

# Leetcode problem 70. Climbing stairs
"""
#Fibonacci sequence but just a little differently done using dynamic programming
def climbStairs(self, n: int) -> int:
	print(n)
	
	# Used a function to define the recursion
	def recursion(n):
	
		# Initialized the list with the first 3, because this sequence is a little different
		f = [0, 1, 2]
		
		# Uses a for loop to save the value into a list and so it reduces runtime instead of
		# having to calculate all the fibonacci numbers before
		for i in range(3, steps+1):
			f.append(f[i-1] + f[i-2])
		
		# returns the f[n] which is the nth value for this problem
		return f[n]
		
	# calls on the recursive function as a return value for this problem
	return recursion(n)

"""


# November 26th 2020
# Leetcode problem 121. Best time to buy and sell stocks
"""
def maxProfit(self, prices: List[int]) -> int:
        
        #print(prices)
        
        if len(prices) < 1:
            return 0
        else:
            buy = prices[0]
            buy_index = 0
            sell_index = 0
            sell = 0
            profit = 0
            best_profit = 0
            
            for i in range(1, len(prices)):
                
                if prices[i] < buy:
                    buy = prices[i]
                    
                if prices[i] - buy > profit:
                    profit = prices[i] - buy
                
                
                best_profit = max(profit, best_profit)
        
        
        if best_profit > 0:
            return best_profit
        else:
            return 0

"""

# Leetcode problem 198. House Robber
"""
def rob(self, nums: List[int]) -> int:
    
	# If length of given array is 0 then just return 0. (no profit)
    if len(nums) == 0:
        return 0
    # If length of array is less or equal to 2, just return the max value
		# of the array
    if len(nums) <= 2:
        return max(nums)
        
    # Initially an empty array size of length of given array
	# first element is same as first element of given array
	# second element of dp is max value between first and second
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
            
	# Loop through length of given array starting from 2nd index and compare
	# which is max value between i-1 value and i-2 value + current value 
	# the higher value will then be added to the dp value for i. 
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
	# return last value of dp array.            
    return dp[-1]

"""

# Leetcode problem 303. Range Sum Qeury - Immutable
# was a little bit and had to look up solutions for this....
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = [0]
        for i in nums:
            self.total.append(self.total[-1]+i)

    def sumRange(self, i: int, j: int) -> int:
        
        return self.total[j+1] - self.total[i]

"""


# Leetcode problem 392. Is subsequence
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        print(s, t)
        
        # to check the index in which the strings of string s were matched in string t
        index_s = [0 for _ in range(len(s))]
        string = [i for i in t]
        count = 0
        
        print('Length of s: {}, Length of t: {}'.format(len(s), len(t)))
        print('string: ',string)
        # if length is equal to 0 just return true
        if len(s) == 0:
            return True
        else: # else go into the loop to find the matches
            for i in range(len(s)):
                # temp is the variable to compare from string s
                temp = s[i]
                # index is the point where the next loop will start off which is the
                # last point in which there was a match
                index = index_s[i-1]
                total_len = len(t)
                
                # loop through string t starting off at index until total length - count
                while index < total_len-count:
                    temp2 = string[index]
                    
                    # if first and second temp match and index_s at i is 0 then switch
                    # from 0 to the index while popping from string list
                    if temp == temp2 and index_s[i] == 0:
                        index_s[i] = index
                        count += 1
                        string.pop(index)
                    else:
                        index += 1
               
                        
                        
            #print(index_s)
            if count == len(s):
                check = sorted(index_s)
                print('Index list: ',index_s)
                if check == index_s:
                    return True
            else:
                return False

"""

# Leetcode problem 746. Min cost climbing stairs
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # added an extra length of 0 for easier calculations for array for saving value and given array
        mincost = [0] * (len(cost)+1)
        cost.append(int(0))
        
        # if length of given array is 2 then return minimal value of two
        if len(cost) == 2:
            return min(cost)
        else:
            # initialize the array for saving value
            mincost[0] = cost[0]
            mincost[1] = cost[1]
            
            for i in range(2, len(cost)):
                #print("Mincost[{}] = min({}, {}+{})".format(i, mincost[i-1], mincost[i-2], cost[i]))
                # the minimal value of adding between i-1 and i-2 is added into the array for saving values
                mincost[i] = min(mincost[i-1] + cost[i], mincost[i-2] + cost[i])
                
                #print('Array Mincost = ', mincost)
                
            # return last value of array which is the value thats added up
            return mincost[-1]

"""

# Leetcode problem 1024. Divisor Game
"""
class Solution:
    def divisorGame(self, N: int) -> bool:
        
        if N % 2 == 0:
            return True
        else:
            return False

"""
