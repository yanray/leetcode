## Rotate Array

### Problem Link

https://leetcode.com/problems/rotate-array/

### Problem Description 

Given an array, rotate the array to the right by k steps, where k is non-negative.

**Follow up:**

* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* Could you do it in-place with O(1) extra space?

**Note:** A leaf is a node with no children.

```
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

```
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

**Constraints:**

* 1 <= nums.length <= 2 * 10^4
* It's guaranteed that nums[i] fits in a 32 bit-signed integer.
* k >= 0

### Code (python)

[Approach 1] (95%)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[: len(nums) - k]
```

[Approach 2] (83% - 95%)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        q = deque(nums)
        for i in range(k):
            q.appendleft(q.pop())
        nums[:] = list(q)[:]
```

Using Cyclic Replacements

[Approach 3] (95%)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1
```

Using Reverse

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

[Approach 4] (83%)

```python
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
```

[Approach 5] (95%)

```python
from collections import deque as dq
class Solution:
    @staticmethod
    def rotate(nums, k):
        deque = dq(nums)
        deque.rotate(k)
        nums[:] = list(deque)
```

https://leetcode.com/problems/rotate-array/discuss/663615/AC-simply-readable-Python-3-solutions-O(1)-space

