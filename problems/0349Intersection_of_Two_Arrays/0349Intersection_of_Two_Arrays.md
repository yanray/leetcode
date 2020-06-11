## Intersection of Two Arrays

### Problem Link

https://leetcode.com/problems/intersection-of-two-arrays/

### Problem Description 

Given two arrays, write a function to compute their intersection.

```
Example 1: 

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

```
Example 1: 

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

```

**Note:**

* Each element in the result must be unique.
* The result can be in any order.

### How to solve 

**Approach 1 - 2:** 
Use set()


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0349Intersection_of_Two_Arrays/0349Intersection_of_Two_Arrays1.py)

```python
return list(set(nums1) & set(nums2))
```


[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0349Intersection_of_Two_Arrays/0349Intersection_of_Two_Arrays2.py)

```python
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
```


[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0349Intersection_of_Two_Arrays/0349Intersection_of_Two_Arrays1.py)

```python

```


[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0349Intersection_of_Two_Arrays/0349Intersection_of_Two_Arrays1.py)

```python

```
