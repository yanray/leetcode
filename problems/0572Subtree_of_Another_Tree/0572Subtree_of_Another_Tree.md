## Subtree of Another Tree

### Problem Link

https://leetcode.com/problems/subtree-of-another-tree/

### Problem Description 

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

```
Example 1:

Given tree s:
     3
    / \
   4   5
  / \
 1   2

 Given tree t:
    4 
  / \
 1   2

 Return true, because t has the same structure and node values with a subtree of s.

```

```
Example 2:

Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2
 Return false.

```


### Code (python)

[Approach 1] (21%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check_tree_same(root1, root2) -> bool:
            
            q = deque()
            q.append([root1, root2])
            
            while q:
                node1, node2 = q.popleft()
                
                if node1.val != node2.val:
                    return False
                if node1.left and node2.left:
                    q.append([node1.left, node2.left])
                if node1.right and node2.right:
                    q.append([node1.right, node2.right])
                
                if (node1.left and not node2.left) or (not node1.left and node2.left) or (node1.right and not node2.right) or (not node1.right and node2.right):
                    return False
                
            return True
        
        if not t:
            return True
        elif not s:
            return False
        
        queue = deque()
        queue.append(s)
        
        while queue:
            node = queue.popleft()
            
            if node.val == t.val:
                if check_tree_same(node, t):
                    return True
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

 
        return False
        
        
        
```

[Approach 2: DFS]

(65%)

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and dfs(s.left, t.left) and dfs(s.right, t.right)

        if not s: return
        if s.val == t.val and dfs(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
```

[Approach 3: to_String] (97%)

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False
    
    
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None
```

```python
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverse_tree(node):
            if not node: return None
            return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
        return traverse_tree(t) in traverse_tree(s)
```

```python
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return 'null'
            tmp = str(root.val) + ','+ dfs(root.left) + ','+  dfs(root.right)
            return ','+tmp+','
        return dfs(s).find(dfs(t)) >= 0
```