"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""

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


if __name__ == '__main__':

    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    stack.top()
    stack.popMax()
    stack.top()
    stack.peekMax()
    stack.pop()
    stack.top()
    
