## Invert Binary Tree

### Problem Link

https://leetcode.com/problems/invert-binary-tree/

### Problem Description 

Invert a binary tree.

```
Example 1:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

```

### Code (python)

[Approach 1] (20%)

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root
        
        output_node = root
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            node.left, node.right = node.right, node.left
            
        return output_node
```