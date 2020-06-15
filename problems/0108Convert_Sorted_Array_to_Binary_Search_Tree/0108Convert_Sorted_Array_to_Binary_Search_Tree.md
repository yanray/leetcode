## Convert Sorted Array to Binary Search Tree

### Problem Link

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

### Problem Description 

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


```
Example 1: 

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

```


### How to solve 

**Approach 1:** 

用hashtable, 类似Two Sum, Two SumII

**Approach 2:** 




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0532Kdiff_Pairs_in_an_Array/0532Kdiff_Pairs_in_an_Array1.py)

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        output = 0
        if k == 0:
            for v in collections.Counter(nums).values():
                if v >= 2:
                    output += 1
            return output
        
        nums.sort()
        
        hash_dict = {}
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] in hash_dict:
                output += 1
            if nums[i] + k <= nums[-1]:
                hash_dict[nums[i] + k] = i
        if nums[-1] in hash_dict:
                output += 1
        
                
        # print(nums)
        # print(hash_dict)
        return output
```

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if not nums or k < 0:
            return 0
        
        output = 0
        if k == 0:
            for v in collections.Counter(nums).values():
                if v >= 2:
                    output += 1
            return output
        
        nums.sort()
        
        hashtable = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] in hashtable:
                output += 1
            if nums[i] + k <= nums[-1]:
                hashtable.append(nums[i] + k)
            while hashtable and nums[i] >= hashtable[0]:
                hashtable.pop(0)
        if nums[-1] in hashtable:
                output += 1
        
                
        # print(nums)
        # print(hashtable)
        return output
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0532Kdiff_Pairs_in_an_Array/0532Kdiff_Pairs_in_an_Array2.py)

```python
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int: 
        
        if not nums or k < 0:
            return 0
        
        nums.sort()

        N = len(nums)

        i = pairs = 0
        j = 1

        while j < N:
            if j < N - 1 and nums[j] == nums[j + 1]:
                j += 1

            elif nums[j] == nums[i] + k:
                pairs += 1
                i += 1
                j += 1

            elif nums[j] > nums[i] + k:
                i += 1

            elif nums[j] < nums[i] + k:
                j += 1

            j = max(j, i + 1)

        return pairs
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0532Kdiff_Pairs_in_an_Array/0532Kdiff_Pairs_in_an_Array3.py)

```python
class Solution(object):
    def findPairs(self, nums, k):
        if k<0:
            return 0
        saw = set()
        diff = set()
        for i in nums:
            if i-k in saw:
                diff.add(i-k)
            if i+k in saw:
                diff.add(i)
            saw.add(i)
        return len(diff)
```