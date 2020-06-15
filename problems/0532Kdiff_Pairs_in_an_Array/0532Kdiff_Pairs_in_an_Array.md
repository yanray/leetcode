## K-diff Pairs in an Array

### Problem Link

https://leetcode.com/problems/k-diff-pairs-in-an-array/

### Problem Description 

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.


```
Example 1: 

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

```

```
Example 2: 

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

```

```
Example 3: 

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

```

**Note:**

1. The pairs (i, j) and (j, i) count as the same pair.
2. The length of the array won't exceed 10,000.
3. All the integers in the given input belong to the range: [-1e7, 1e7].

### How to solve 

**Approach 1:** 

用hashtable, 类似Two Sum, Two SumII

**Approach 2:** 

Use two Pointers 

**Approach 3:** 

Use set()



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