## Diameter of Binary Tree

### Problem Link
https://leetcode.com/problems/diameter-of-binary-tree/

### Problem Description 

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


```
Example 1:

Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
```
**Note:** The length of path between two nodes is represented by the number of edges between them.

### How to solve 

**Approach 1:** 

counting edges(left, right) to find the longest path

**Approach 2:** 
counting nodes to find the longest path, (number of nodes - 1)


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
