## Max Stack

### Problem Link

https://leetcode.com/problems/max-stack/

### Problem Description 

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

```
Example 1: 

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

```

**Note:**

1. -1e7 <= x <= 1e7
2. Number of operations won't exceed 10000.
3. The last four operations won't be called when stack is empty.

### How to solve 

**Approach 1:** 


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0716Max_Stack/0716Max_Stack1.py)

```python
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def peekMax(self) -> int:
        if len(self.stack) > 0:
            return max(self.stack)

    def popMax(self) -> int:
        if len(self.stack) > 0:
            max_val = max(self.stack)
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i] == max_val:
                    return self.stack.pop(i)
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0716Max_Stack/0716Max_Stack2.py)

```python
class DoubleLinkedNode:
    def __init__(self, value, heap_idx, prev=None, nxt=None):
        self.value = value
        self.heap_idx = heap_idx
        self.prev = prev
        self.next = nxt


class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # create dummy nodes for head and tail of DLL
        self.head = DoubleLinkedNode(None, None)        
        self.tail = DoubleLinkedNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

        # underlying list to be used as a min heap
        self.heap = []

        # running counter added to heap keys to handle key duplicates
        self.items_pushed = 0

    def push(self, x: int) -> None:
        # push node as head of DLL
        node = DoubleLinkedNode(x, len(self.heap), prev=self.head, nxt=self.head.next)
        self.head.next.prev = self.head.next = node

        # push a pointer to node to heap
        self.heap.append((-x, -self.items_pushed, node))
        self._siftdown(0, len(self.heap)-1)

        self.items_pushed += 1

    def pop(self) -> int:
        # pop and detach head from DLL
        node = self.head.next
        node.prev.next, node.next.prev = node.next, node.prev

        # pop arbitrary element at index <node.heap_idx> from heap, and update heap
        self.heap[node.heap_idx] = self.heap[-1]
        self.heap.pop()
        if node.heap_idx < len(self.heap):
            self._siftup(node.heap_idx)
            self._siftdown(0, node.heap_idx)

        return node.value

    def top(self) -> int:
        return self.head.next.value

    def peekMax(self) -> int:
        return self.heap[0][2].value

    def popMax(self) -> int:
        # peek at max tuple in the heap, use its node pointer
        node = self.heap[0][2]

        # heappop
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._siftup(0)

        # pop and detach node from DLL
        node.prev.next, node.next.prev = node.next, node.prev

        return node.value

    def _siftdown(self, startpos, pos):
        """ modified from heapq library to update DLL node pointers on every change in heap order """
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                # update node heap_idx pointer
                parent[2].heap_idx = pos    
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
        # update node heap_idx pointer
        self.heap[pos][2].heap_idx = pos   

    def _siftup(self, pos):
        """ modified from heapq library to update DLL node pointers on every change in heap order """
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[childpos]
            # update node heap_idx pointer
            self.heap[pos][2].heap_idx = pos
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        # update node heap_idx pointer
        self.heap[pos][2].heap_idx = pos
        self._siftdown(startpos, pos)
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0716Max_Stack/0716Max_Stack3.py)

```python

```