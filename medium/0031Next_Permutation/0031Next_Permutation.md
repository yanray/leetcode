## Next Permutation

### Problem Link

https://leetcode.com/problems/next-permutation/

### Problem Description 

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
Example 1:

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

```

### Code (python)

[Approach 1] (92% - 98%)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return 
        
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return 
        
        heap = []
        change_index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                heapq.heappush(heap, nums[i])
                change_index = i - 1
                break
            else:
                heapq.heappush(heap, nums[i])

        if change_index == -1:
        	for i in range(len(nums) // 2):
        		nums[i], nums[~i] = nums[~i], nums[i]
        	return 
                
        temp_list = []
        for i in range(len(heap)):
            temp = heapq.heappop(heap)
            if nums[change_index] >= temp:
                temp_list.append(temp)
            else:
                heapq.heappush(heap, nums[change_index])
                nums[change_index] = temp
                break
        
        nums[change_index + 1 : change_index + 1 + len(temp_list)] = temp_list[:]
        len_heap = len(heap)
        for i in range(len_heap):
            nums[len(nums) - len_heap + i] = heapq.heappop(heap)
```

[Approach 2] (77%)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k, l = len(nums) -2 , len(nums) - 1
        while k >= 0 and nums[k] >= nums[k+1]:
            k -= 1
        if k == -1:
            return nums.reverse()
        while nums[k] >= nums[l]:
            l -= 1
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:]=reversed(nums[k+1:])
```

```python
class Solution:
    
    def max_from_right(self, nums):
        j = len(nums) - 1
        while j > 0:
            if nums[j - 1] < nums[j]:
                return j
            j -= 1
        return 0
    
    def swap_candidate(self, nums, x):
        j = len(nums) - 1
        while j>=0 and nums[j] <= x:
            j -= 1
        return j
    
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peek = self.max_from_right(nums)
        if peek == 0:
            return nums.sort()
        
        i, x = peek - 1, nums[peek-1]
        j = self.swap_candidate(nums, x)
        nums[i], nums[j] = nums[j], nums[i]
        nums[peek:] = reversed(nums[peek:])
```