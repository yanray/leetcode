## Design HashMap

### Problem Link
https://leetcode.com/problems/design-hashmap/

### Problem Description 

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

* put(key, value) : Insert a (key, value) pair into the HashMap. If the value already &* exists in the HashMap, update the value.
* get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
* remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.



```
Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

```


### How to solve 

**Approach 1:** 

Use Dictionary, however, this is wrong in this question 

**Approach 2:** 

Build a bucket to store (key, value), use prime number 2069 to map hash key number, corresponding to different buckets. 

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary1.py)

```python
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        if key in self.dict:
            self.dict[key] = value
        else:
            self.dict[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        if key in self.dict:
            return self.dict[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        if key in self.dict:
            del self.dict[key]
        
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary2.py)

```python
hashmap = {c:i for i, c in enumerate(order)}
return words == sorted(words, key = lambda w: [hashmap[x] for x in w])
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary3.py)

```python
return words == sorted(words, key = lambda w: [order.index(x) for x in w])
```