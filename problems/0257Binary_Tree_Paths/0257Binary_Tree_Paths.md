## Binary Tree Paths

### Problem Link

https://leetcode.com/problems/binary-tree-paths/

### Problem Description 

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

```
Example 1:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

```

### Code (python)

[Approach 1] (50%)  O(N)

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root:
            return []
        
        result = []
        q = deque()
        q.append((root, ""))
        
        while q:
            node, path = q.popleft()
            
            if not node.left and not node.right:
                result.append(path + str(node.val))
                
            if node.right:
                q.appendleft((node.right, path + str(node.val) + "->"))
            if node.left:
                q.appendleft((node.left, path + str(node.val) + "->" ))
                
                
        return result
```

[Approach 2: Recursion] (50%)  O(N)

```python
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths  
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
```

[Approach 3] (%)

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return [f'{root.val}->{path}' 
                for path in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)] \
                or [f'{root.val}']
```