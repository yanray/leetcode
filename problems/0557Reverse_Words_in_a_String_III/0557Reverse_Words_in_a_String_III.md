## Find All Numbers Disappeared in an Array

### Problem Link

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

### Problem Description 

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

```
Example 1:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

```

### Code (python)

[Approach 1] (65%)

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        result = []
        curr_val = 1
        for i in range(len(nums)):
            if curr_val == nums[i]:
                curr_val += 1
                continue
            elif curr_val < nums[i]:
                result.append(curr_val)
                curr_val += 1
                while curr_val < nums[i]:
                    result.append(curr_val)
                    curr_val += 1
                curr_val += 1
                
        while curr_val <= len(nums):
            result.append(curr_val)
            curr_val += 1
    
        return result
```

[Approach 2: Using Hash Map] (20%)

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result
```

[Approach 3: O(1) Space InPlace Modification Solution] (26%)

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result        
```

(38%)

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ## RC ##
        ## APPROACH : INDEX AS HASH KEY ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        ans = []
        for i in range(len(nums)):
            if( not nums[abs(nums[i]) - 1] < 0 ): nums[abs(nums[i]) - 1] *= -1
        for i,num in enumerate(nums):
            if( num > 0 ): ans.append(i + 1)
        return ans
```