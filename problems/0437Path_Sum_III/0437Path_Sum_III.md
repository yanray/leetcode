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



### Code (python)

[Approach 1] (45%)

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

[Approach 2] (95%)

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ## RC ##
        ## APPROACH : RECURSION ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        def helper(node, val, lookup):
            
            if(not node): return
            val += node.val
            if(val == sum): self.ans += 1
            if((val-sum) in lookup and lookup[val - sum] > 0):
                self.ans += lookup[val - sum]                     # watchout, lookup[val-sum]
            lookup[val] += 1
            if(node.left): 
                helper(node.left, val, lookup)
            if(node.right): 
                helper(node.right , val, lookup)
            lookup[val] -= 1                                    # if we first move to left side and come back to right side, left side subarray sums shouldn't be there in right side, so backtracking lookup.
            
        self.ans = 0
        helper(root, 0, collections.defaultdict(int) )
        return self.ans
```


[Approach 2] (91%)

```python
from collections import Counter

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def pathSumSearch(node: TreeNode, cumsum: int) -> int:
            if not node:
                return 0
            
            # add up paths up to <node> and add current cumsum to <prefixes>
            cumsum += node.val
            paths_to_node = prefixes[cumsum - sum]
            prefixes[cumsum] += 1
            
            # going down the tree
            paths_to_children = pathSumSearch(node.left, cumsum) + pathSumSearch(node.right, cumsum)
            
            # going up the tree (remove current cumsum from <prefixes> so non-children won't use it)
            prefixes[cumsum] -= 1
            return paths_to_node + paths_to_children
        
        prefixes = Counter({0: 1})
        return pathSumSearch(root, 0)
```