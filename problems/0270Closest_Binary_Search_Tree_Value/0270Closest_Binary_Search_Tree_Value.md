## Closest Binary Search Tree Value

### Problem Link

https://leetcode.com/problems/closest-binary-search-tree-value/

### Problem Description 

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

**Note:**

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

```
Example 1:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

```

### Code (python)

[Approach 1] (>90%)

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        if not root:
            return None
        
        q = deque()
        q.append(root)
        closest = abs(root.val - target)
        closest_val = root.val
        
        while q:
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            if abs(node.val - target) < closest:
                closest = abs(node.val - target)
                closest_val = node.val
                
                # if closest < 0.5:
                #     return closest_val
                
        return closest_val
```

[Approach 2] (>90%)

Recursive Inorder + Linear search, O(N) time

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
```

[Approach 3] (75%)

Recursive Inorder + Linear search, O(N) time

```python
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
```


https://leetcode.com/problems/closest-binary-search-tree-value/solution/

https://leetcode.com/problems/closest-binary-search-tree-value/discuss/636888/AC-simply-readable-Python-2-solutions

