## Intersection of Two Arrays II

### Problem Link

https://leetcode.com/problems/intersection-of-two-arrays-ii/

### Problem Description 

Given two arrays, write a function to compute their intersection.

```
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

```
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

```

**Note:**

* Each element in the result should appear as many times as it shows in both arrays.
* The result can be in any order.

**Follow up:**

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


### Code (python)

[Approach 1] (77%)

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        
        nums1.sort()
        nums2.sort()
        
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
                
        return result
```

https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/607702/Python-O(m%2Bn)-sol-by-native-Counter-w-Comment

[Approach 2] (94)

```python
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        # keep the smallest as nums1
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        # save in a multiset the smallest
        counter = Counter(nums1)
        # find matches, removing from counter when found
        output = []
        for e in nums2:
            if counter[e] > 0:
                output.append(e)
                counter[e] -= 1
        return output
```

```python
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        res = []
        
        if len(nums1)>=len(nums2):
            bigger = collections.Counter(nums1)
            smaller = nums2
        else:
            bigger = collections.Counter(nums2)
            smaller = nums1
            
        for i in smaller:
            if bigger.get(i,0)>0:
                bigger[i]-=1
                res.append(i)
                
        return res
```

https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/507788/Summary-from-the-original-problem-to-follow-ups