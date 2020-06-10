## LRU Cache

### Problem Link

https://leetcode.com/problems/lru-cache/

### Problem Description 

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

* get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
* put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

**Follow up:**
Could you do both operations in O(1) time complexity?

```
Example: 

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

```

### How to solve 

**Approach 1:** 

Ordered dictionary

**Approach 2:** 

Hashmap + DoubleLinkedList


### Code (python)

[Approach 1]

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        
        self.cache_dict.move_to_end(key)
        return self.cache_dict[key]
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache_dict:
            self.cache_dict.move_to_end(key)
        self.cache_dict[key] = value
        if len(self.cache_dict) > self.cap:
            self.cache_dict.popitem(last = False)
```

[Approach 2]

```python
class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)
```

[Approach 3]

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.cap = capacity
            

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        val = self.cache_dict.pop(key)
        self.cache_dict[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_dict:
            if len(self.cache_dict) < self.cap:
                self.cache_dict[key] = value
            else:
                self.cache_dict.pop(list(self.cache_dict.keys())[0])
                self.cache_dict[key] = value
        else:
            self.cache_dict.pop(key)
            self.cache_dict[key] = value
```

[Approach 4]

```python
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dum = ListNode((-1,-1))
        self.tail = None
        self.mapp = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        else:
            (x,y) = self.mapp[key].next.value
            self.remove(x)
            self.insertHead(x, y)
            return y
        
    def put(self, key: int, val: int) -> None:
        if self.get(key) == -1:
            self.insertHead(key, val)
            if self.size > self.cap:
                #should only remove tail!
                self.remove(self.tail)
        else:
            self.remove(key)
            self.insertHead(key, val)
            
    def insertHead(self, key, value):
        if self.size == 0:
            self.tail = key

        # insert to linked list head 
        newNode =  ListNode((key,value))
        temp = self.dum.next
        self.dum.next = newNode
        newNode.next = temp
        
        # insert to map:
        self.mapp[key] = self.dum
        
        # update mapp[temp] to the previous node of temp
        if temp != None:
            self.mapp[temp.value[0]] = newNode
    
        self.size += 1 
        
        
    def remove(self, key):
        prev = self.mapp[key]
        prev.next = prev.next.next
        
        #update nextnode's pointing
        if prev.next:
            nextNode = prev.next.value[0]
            self.mapp[nextNode] = prev
        
        if key == self.tail:
            #update the tail
            self.tail = prev.value[0]
            
        del self.mapp[key]
        self.size -= 1
```
