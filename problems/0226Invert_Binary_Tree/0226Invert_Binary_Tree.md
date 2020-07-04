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

[Approach 2: Recursive] (O(N))

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        ## RC ##
        ## APPROACH : RECURSION ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        def dfs(root):
            if root:
                root.left, root.right   = dfs(root.right), dfs(root.left)
            return root
        return dfs(root)
```

https://leetcode.com/problems/invert-binary-tree/discuss/664132/Python-O(n)-by-DFS-BFS-w-Visualization-90%2B

[Approach 3: Recursive] (O(N))

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root:
            # General case:
            
            # invert child node of current root
            root.left, root.right = root.right, root.left
            
            # invert subtree with DFS
            
            if root.left:
                self.invertTree( root.left )
            
            if root.right:
                self.invertTree( root.right )
            
            return root
        
        else:
            # Base case:
            # empty tree
            
            return None
```
