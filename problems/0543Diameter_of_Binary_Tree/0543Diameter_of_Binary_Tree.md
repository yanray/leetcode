## Move Zeroes

### Problem Link
https://leetcode.com/problems/move-zeroes/

### Problem Description 

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


```
Example 1:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### How to solve 

**Approach 1:** 

找0, remove, del or pop, then append(0)

**Approach 2:** 

找两个pointer, slow and fast, slow pointer 不是0 就替换

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0283Move_Zeroes/0283Move_Zeroes1.py)

```python
i = 0
length = len(nums)
while i < length:
    if nums[i] == 0:
        del nums[i]
        nums.append(0)
        length -= 1
    else:
        i += 1
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0283Move_Zeroes/0283Move_Zeroes2.py)

```python
slow, fast = 0, 0
length = len(nums)
for fast in range(length): 
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
```
