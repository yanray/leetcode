## Binary Tree Right Side View

### Problem Link

https://leetcode.com/problems/binary-tree-right-side-view/

### Problem Description 

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

```
Example 1:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

```


### Code (python)

[Approach 1] (50%) 

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if not root:
            return root
        
        q = deque()
        q.append([root, 1])
        
        result = []
        pre_val = root.val
        pre_layer = 1
        
        while q:
            node, curr_layer = q.popleft()
            
            if pre_layer != curr_layer:
                pre_layer = curr_layer
                result.append(pre_val)
            pre_val = node.val
            
            if node.left:
                q.append([node.left, curr_layer + 1])
            if node.right:
                q.append([node.right, curr_layer + 1])
        result.append(pre_val)        
        
        return result
```

[Approach 2: BFS: Two Queues]

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                    
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)
        
        return rightside
```


[Approach 3: BFS: One Queue + Sentinel]

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root, None,])
        rightside = []
        
        curr = root
        while queue:
            prev, curr = curr, queue.popleft()

            while curr:
                # add child nodes in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
                prev, curr = curr, queue.popleft()
            
            # the current level is finished
            # and prev is its rightmost element      
            rightside.append(prev.val)
            # add a sentinel to mark the end 
            # of the next level
            if queue:
                queue.append(None)
        
        return rightside
```

[Approach 4: BFS: One Queue + Level Size Measurements]

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root,])
        rightside = []
        
        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)
                    
                # add child nodes in the queue 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rightside
```

[Approach 5: Recursive DFS] (78%)

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        rightside = []
        
        def helper(node: TreeNode, level: int) -> None:
            if level == len(rightside):
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
                
        helper(root, 0)
        return rightside
```