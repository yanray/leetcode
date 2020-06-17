## Path Sum III

### Problem Link

https://leetcode.com/problems/path-sum-iii/

### Problem Description 

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.


```
Example 1: 

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```


### How to solve 

**Approach 1:** 

**Approach 2:** 



### Code (python)

[Approach 1]

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            return 0
        
        q = deque()
        q.append((root, []))
        
        counter = 0
        while q:
            node, path = q.popleft()

            for i in range(len(path)):
                if path[i] + node.val == sum:
                    counter += 1
                path[i] += node.val
            if node.val == sum:
                counter += 1

            if node.right:
                q.appendleft((node.right, path + [node.val]))
            if node.left:
                q.appendleft((node.left, path + [node.val]))
                
        return counter
```

[Approach 2]

```python

```