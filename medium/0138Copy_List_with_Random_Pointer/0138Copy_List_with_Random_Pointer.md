## Copy List with Random Pointer

### Problem Link

https://leetcode.com/problems/copy-list-with-random-pointer/

### Problem Description 

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


### Code (python)

[Approach 1] (93%) 

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        hash_dict = {}
        dummy = new_head = None
        temp = head
        while temp:
            if new_head:
                new_head.next = Node(temp.val)
                new_head = new_head.next
            else:
                dummy = new_head = Node(temp.val)
            hash_dict[temp] = new_head
            temp = temp.next

        temp = head
        new_head = dummy
        while temp:
            rand_node = temp.random
            if rand_node:
                new_head.random = hash_dict[rand_node]
            new_head = new_head.next
            temp = temp.next
            
        return dummy
```

[Approach 2: Recursive]

```python
class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
```