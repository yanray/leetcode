## Maximum Depth of Binary Tree

### Problem Link

https://leetcode.com/problems/maximum-depth-of-binary-tree/

### Problem Description 

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note:** A leaf is a node with no children.

```
Example 1:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

```

### Code (python)

[Approach 1] (78%)

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def DFS(root, depth):
            
            self.max_depth = max(self.max_depth, depth)
            if root.left:
                DFS(root.left, depth + 1)
            if root.right:
                DFS(root.right, depth + 1)
                
            
        if not root:
            return 0
            
        self.max_depth = 0
        DFS(root, 1)
        
        return self.max_depth
```

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ## RC ##
        ## APPROACH : DFS ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        def helper(node):
            if(not node):   return 0
            l = r = 0
            if(node.left):
                l = max(helper(node.left), 0)
            if(node.right):
                r = max(helper(node.right), 0)
            return 1 + max(l, r)
        return helper(root)
```

[Approach 2] (%)

```python

```

