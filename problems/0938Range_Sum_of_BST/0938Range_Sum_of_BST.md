## Range Sum of BST

### Problem Link

https://leetcode.com/problems/range-sum-of-bst/

### Problem Description 

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


```
Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

```

```
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

```

**Note:**

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

### Code (python)

[Approach 1] (50%)

```python
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if not root:
            return 0
        
        q = [root]
        sum_BST = 0
        
        while q:
            node = q.pop()
            
            if node.val >= L and node.val <= R:
                sum_BST += node.val
                
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return sum_BST
```

[Approach 2] (85%) (fast)

```python
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
```

[Approach 3] (75%)

```python
class Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
```