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

[Approach 1] (98%)

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