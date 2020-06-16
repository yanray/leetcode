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

DFS, 把相对应的sum值也append到deque()

**Approach 2:** 

Recursion

**Approach 3:** 

Iteration, kind of similar to approach 1

### Code (python)

[Approach 1]

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        q = deque()
        q.append((root, 0))
        
        while q:
            node, val = q.popleft()
            
            if not node.left and not node.right and val + node.val == sum:
                return True
            
            if node.right:
                q.appendleft((node.right, val + node.val))
            if node.left:
                q.appendleft((node.left, val + node.val))
                
        return False
```

[Approach 2]

```python
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

[Approach 3]

```python
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
```