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

