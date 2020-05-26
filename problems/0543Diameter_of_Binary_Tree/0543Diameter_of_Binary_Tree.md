## Diameter of Binary Tree

### Problem Link
https://leetcode.com/problems/diameter-of-binary-tree/

### Problem Description 

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


```
Example 1:

Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
```
**Note:** The length of path between two nodes is represented by the number of edges between them.

### How to solve 

**Approach 1:** 

counting edges(left, right) to find the longest path

**Approach 2:** 
counting nodes to find the longest path, (number of nodes - 1)


### Code (python)

[Approach 1]

```python
self.max_diameter = 0

def depth(tree):
    if not tree:
        return 0
    
    L_dep = depth(tree.left)
    R_dep = depth(tree.right)
    self.max_diameter = max(self.max_diameter, L_dep + R_dep)
    return max(L_dep, R_dep) + 1

depth(root)

return self.max_diameter
```

[Approach 2]

```python
self.max_diameter = 1

def depth(tree):
    if not tree:
        return 0
    
    L_dep = depth(tree.left)
    R_dep = depth(tree.right)
    self.max_diameter = max(self.max_diameter, L_dep + R_dep + 1)
    return max(L_dep, R_dep) + 1

depth(root)

return self.max_diameter - 1
```
