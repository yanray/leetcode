## Symmetric Tree

### Problem Link

https://leetcode.com/problems/symmetric-tree/

### Problem Description 

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

```
Example 1: 

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

```

```
Example 2: 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

```

### How to solve 

**Approach 1:** 

recursive: 判断root 是否相等, 如果相等, 判断子数是否对称

**Approach 2:** 

iterative, almost same as approach 1

**Approach 3 - 4:** 

BFS, 逐行判断

**Approach 5:** 

DFS

### Code (python)

[Approach 1] (24ms)

```python
def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

return isMirror(root, root)
```


[Approach 2]

```python
tree_queue = deque()
tree_queue.append(root)
tree_queue.append(root)

while tree_queue:
    q1 = tree_queue.popleft()
    q2 = tree_queue.popleft()
    
    if not q1 and not q2:
        continue
    elif not q1 or not q2:
        return False
    elif q1.val != q2.val:
        return False
    else:
        tree_queue.append(q1.left)
        tree_queue.append(q2.right)
        tree_queue.append(q1.right)
        tree_queue.append(q2.left)
return True
```


[Approach 3]

```python
if not root:
    return True

depth_vals = defaultdict(list)        
queue = [(root, 0)]
curr_depth = 0
for node, depth in queue:
    if not node:
        depth_vals[depth].append(None)
    if node:
        depth_vals[depth].append(node.val)
        queue.append((node.left, depth+1))
        queue.append((node.right, depth+1))
    if depth > curr_depth:
        if depth_vals[curr_depth] != depth_vals[curr_depth][::-1]:
            return False
        else:
            curr_depth = depth
else:
    return True
```


[Approach 4]

```python
queue = [root]

while(queue):
    next_queue = list()
    layer = list()
    for node in queue:
        if not node:
            layer.append(None)
            continue
        next_queue.append(node.left)
        next_queue.append(node.right)
        
        layer.append(node.val)
        
    if layer != layer[::-1]:
        return False
    queue = next_queue
    
return True
```


[Approach 5]

```python
path = []
def euler(node):
    if not node: path.append(None); return
    path.append(node.val)
    euler(node.left)
    # path.append(node.val)
    euler(node.right)
    path.append(node.val)
euler(root)
return path == path[::-1]
```