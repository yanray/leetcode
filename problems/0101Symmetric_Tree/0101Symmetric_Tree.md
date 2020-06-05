## Symmetric Tree

### Problem Link

https://leetcode.com/problems/symmetric-tree/

### Problem Description 

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

```
Example 1: 

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

```

```
Example 2: 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

```

### How to solve 

**Approach 1:** 

recursive: 判断root 是否相等, 如果相等, 判断子数是否对称

**Approach 2:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0101Symmetric_Tree/0101Symmetric_Tree1.py)

```python
def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

return isMirror(root, root)
```
