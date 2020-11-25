

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
