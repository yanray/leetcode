## Subarray Sum Equals K

### Problem Link

https://leetcode.com/problems/subarray-sum-equals-k/

### Problem Description 

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

```
Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

```

**Constraints:**

* The length of the array is in range [1, 20,000].
* The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

### Code (python)

[5 approaches](https://leetcode.com/problems/subarray-sum-equals-k/discuss/503178/Python5-Approaches-easy-to-understand-with-detailed-explanations)

[Approach 1] (35% - 66%)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hash_table = collections.defaultdict(int)
        
        total = 0
        count_sub = 0
        for i in range(len(nums)):
            total += nums[i]
            
            if total == k:
                count_sub += 1
            if (total - k) in hash_table:
                count_sub += hash_table[total - k]
            hash_table[total] += 1
            
        return count_sub
```

[Approach 2] (30%)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen_sums = defaultdict(int)
        
        for acc in accumulate(nums, initial=0):
            count += seen_sums[acc - k]
            seen_sums[acc] += 1
        
        return count
```

[Approach 3] (30% - 40%)

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
```