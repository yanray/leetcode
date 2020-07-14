## Next Greater Element I

### Problem Link

https://leetcode.com/problems/next-greater-element-i/

### Problem Description 

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

```
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

```

```
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

```

**Note:**

1. All elements in nums1 and nums2 are unique.
2. The length of both nums1 and nums2 would not exceed 1000.


### Code (python)

[Approach 1] (80%) 

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_dict = {}
        
        for i in range(len(nums2)):
            hash_dict[nums2[i]] = i
            
        for i in range(len(nums1)):
            index = hash_dict[nums1[i]] + 1
            
            while index < len(nums2) and nums1[i] > nums2[index]:
                index += 1
                
            if index == len(nums2):
                nums1[i] = -1
            else:
                nums1[i] = nums2[index]
                
        return nums1
```

[Approach 2] (%)  (O(m + n))

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = {}
        stack = []
        for n in nums2:
            while stack and stack[-1]<n:
                next_greater[stack.pop()] = n
            stack.append(n)
        return [next_greater.get(n, -1) for n in nums1]
```