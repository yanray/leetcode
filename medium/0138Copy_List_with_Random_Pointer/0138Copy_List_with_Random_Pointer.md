## Permutations

### Problem Link

https://leetcode.com/problems/permutations/

### Problem Description 

Given a collection of distinct integers, return all possible permutations.

```
Example 1:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```

### Code (python)

[Approach 1] (5%) 

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def nextPermutation(nums: List[int]):
            
            result = copy.deepcopy(nums)
            
            k, l = len(result) -2 , len(result) - 1
            while k >= 0 and result[k] >= result[k+1]:
                k -= 1
            if k == -1:
                return result[::-1]
            while result[k] >= result[l]:
                l -= 1
            result[k], result[l] = result[l], result[k]
            result[k+1:]=reversed(result[k+1:])
            
            return result
        
        if not nums:
            return nums
        
        result = []
        result.append(nums)
        temp = nextPermutation(nums)

        while nums != temp:
            result.append(temp)
            temp = nextPermutation(temp)
        
        return result
```

[Approach 2: Backtracking] (32%)

```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output
```

```python
class Solution:
    def permute(self, arr):
        output = []
        result = []
        self.permuteHelper(arr, output, result)
        return result

    def permuteHelper(self, arr, output, result):
        if not arr:
        # print(output)
            result.append(output[:])
        else:
            for i in range(len(arr)):
                item = arr.pop(i)
                # print(arr)
                output.append(item)
                self.permuteHelper(arr, output, result)
                output.pop()
                arr.insert(i, item)
```

```python
def permute(self, nums: List[int]) -> List[List[int]]:
	result = []
	def backtrace(nums, path):
		if len(path)==len(nums):
			result.append(path[:])
			return
		for num in nums:
			if num not in path:
				path.append(num)
				backtrace(nums, path)
				path.pop()
	backtrace(nums, [])
	return result
```

https://leetcode.com/problems/permutations/discuss/711899/Faster-than-99.5-short-python3-code-with-pop()-and-insert.

https://leetcode.com/problems/permutations/discuss/?currentPage=1&orderBy=hot&query=&tag=python