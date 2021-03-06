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

总是选择middle作为root, 如果list长度为1, return这个node, 如果为空, return None, 左子数和右子数只需要递归传入相应的子list即可

**Approach 2:** 

Always Choose Left Middle Node as a Root:

* Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

    - If left > right, then there is no elements available for that subtree. Return None.

    - Pick left middle element: p = (left + right) // 2.

    - Initiate the root: root = TreeNode(nums[p]).

    - Compute recursively left and right subtrees: root.left = helper(left, p - 1), root.right = helper(p + 1, right).

* Return helper(0, len(nums) - 1).

**Approach 3:** 

Always Choose Right Middle Node as a Root:

* Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

    - If left > right, then there is no elements available for that subtree. Return None.

    - Pick right middle element:

        - p = (left + right) // 2.

        - If left + right is odd, add 1 to p-index.

    - Initiate the root: root = TreeNode(nums[p]).

    - Compute recursively left and right subtrees: root.left = helper(left, p - 1), root.right = helper(p + 1, right).

* Return helper(0, len(nums) - 1).


**Approach 3:**

Choose Random Middle Node as a Root:

* Implement helper function helper(left, right), which constructs BST from nums elements between indexes left and right:

    - If left > right, then there is no elements available for that subtree. Return None.

    - Pick random middle element:

        - p = (left + right) // 2.

        - If left + right is odd, add randomly 0 or 1 to p-index.

    - Initiate the root: root = TreeNode(nums[p]).

    - Compute recursively left and right subtrees: root.left = helper(left, p - 1), root.right = helper(p + 1, right).

* Return helper(0, len(nums) - 1).

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