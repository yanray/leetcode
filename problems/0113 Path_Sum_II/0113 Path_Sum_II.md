## Path Sum II

### Problem Link

https://leetcode.com/problems/path-sum-ii/

### Problem Description 

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.


```
Example 1: 

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return
[
   [5,4,11,2],
   [5,8,4,5]
]
```


### How to solve 

**Approach 1:** 

DFS with deque()

**Approach 2:** 

Recursion


### Code (python)

[Approach 1]

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque()
        q.append((root, 0, []))
        
        path_list = []
        while q:
            node, val, path = q.popleft()
            
            if not node.left and not node.right and val + node.val == sum:
                path_list.append(path + [node.val])

            if node.right:
                q.appendleft((node.right, val + node.val, path + [node.val]))
            if node.left:
                q.appendleft((node.left, val + node.val, path + [node.val]))
                
        return path_list
```

[Approach 2]

```python
class Solution:

    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        
        if not node:
            return 
        
        # Add the current node to the path's list
        pathNodes.append(node.val)
        
        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            
        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList
```