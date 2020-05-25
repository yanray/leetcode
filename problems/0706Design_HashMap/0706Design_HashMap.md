## Design HashMap

### Problem Link

https://leetcode.com/problems/design-hashmap/

### Problem Description 

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

* put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
* get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
* remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.



```
Example 1:

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

Use Dictionary, however, it's wrong

**Approach 2:** 

Use Bucket and a prime number 2069 to map key into different buckets.



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0706Design_HashMap/0706Design_HashMap1.py)

```python
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


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0706Design_HashMap/0706Design_HashMap2.py)

```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keuy_space_num = 2069
        self.hashtable = [Bucket() for i in range(self.keuy_space_num)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        hash_key = key % self.keuy_space_num
        self.hashtable[hash_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        hash_key = key % self.keuy_space_num
        return self.hashtable[hash_key].get(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        
        hash_key = key % self.keuy_space_num
        self.hashtable[hash_key].remove(key)
        

        
class Bucket: 
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
    	found = False
    	for i, key_value in enumerate(self.bucket):
    		if key_value[0] == key:
    			self.bucket[i] = (key, value)
    			found = True
    			# print('i', i)
    			# print('key_value', key_value)

    	if not found: 
    		self.bucket.append((key, value))

    	# print(self.bucket)

    def get(self, key):
    	for (k, v) in self.bucket:
    		if k == key:
    			return v

    	return -1

    def remove(self, key):
    	for i, key_value in enumerate(self.bucket):
    		if key_value[0] == key:
    			del self.bucket[i]

```

