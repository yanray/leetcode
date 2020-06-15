## Path Sum

### Problem Link

https://leetcode.com/problems/path-sum/

### Problem Description 

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.


```
Example 1: 

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
```


### How to solve 

**Approach 1:** 



### Code (python)

[Approach 1]

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            
            middle = len(nums) // 2  
            node = TreeNode(nums[middle])
            node.left = helper(nums[0 : middle])
            node.right = helper(nums[middle + 1 :])
            return node
        
        return helper(nums)
```

[Approach 2]

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = left + (left - right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
```

[Approach 3]

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None
            
            # always choose right middle node as a root
            p = (left + right) // 2 
            if (left + right) % 2:
                p += 1 

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
```

[Approach 3]

```python
from random import randint
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None
            
            # choose random middle node as a root
            p = (left + right) // 2 
            if (left + right) % 2:
                p += randint(0, 1) 

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
```