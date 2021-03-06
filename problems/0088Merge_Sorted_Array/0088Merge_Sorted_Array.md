## Merge Sorted Array

### Problem Link
https://leetcode.com/problems/verifying-an-alien-dictionary/

### Problem Description 

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

**Note:**

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

```
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

```

### How to solve 

**Approach 1:** 

Two pointers, one to nums1, the other to nums2, 

循环比较大小 (from start to end)

**Approach 2:** 

Two pointers, (from end to start)

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0088Merge_Sorted_Array/0088Merge_Sorted_Array1.py)

```python
nums1[:] = sorted(nums1[:m] + nums2)
```
[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0088Merge_Sorted_Array/0088Merge_Sorted_Array2.py)

```python
nums1_cp = nums1[:m]
nums1[:] = []

p1 = 0
p2 = 0
while p1 < m and p2 < n:
    if nums1_cp[p1] < nums2[p2]:
        nums1.append(nums1_cp[p1])
        p1 += 1
    else:
        nums1.append(nums2[p2])
        p2 += 1
        
if p1 < m:
    nums1[p1 + p2 :] = nums1_cp[p1 :]
else:
    nums1[p1 + p2 :] = nums2[p2 :]
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0088Merge_Sorted_Array/0088Merge_Sorted_Array3.py)

```python
p1 = m - 1
p2 = n - 1
p = m + n -1

while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
    p -= 1
    
if p2 >= 0:
    nums1[: p2 + 1] = nums2[: p2 + 1]
```