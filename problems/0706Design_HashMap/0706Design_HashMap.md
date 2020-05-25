## Subdomain Visit Count

### Problem Link
https://leetcode.com/problems/subdomain-visit-count/

### Problem Description 

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.


```
Example 1:

Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

```


```
Example 2:

Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

```


### How to solve 

**Approach 1:** 

Use Dictionary, however, this is wrong in this question 

**Approach 2:** 

Build a bucket to store (key, value), use prime number 2069 to map hash key number, corresponding to different buckets. 

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0706Design_HashMap/0706Design_HashMap1.py)

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

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0706Design_HashMap/0706Design_HashMap2.py)

```python
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


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space_num = 2069
        self.hashtable = [Bucket() for i in range(self.key_space_num)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        hash_key = key % self.key_space_num
        self.hashtable[hash_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space_num
        return self.hashtable[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space_num
        self.hashtable[hash_key].remove(key)
```