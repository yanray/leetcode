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

Use dictionary, split visit times and domain, extract all subdomain

**Approach 2:** 
Use collections.Counter()



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count1.py)

```python
sub_domain = {}
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)
    sub_d = domain.split('.')
    
    sub_d_length = len(sub_d)
    for j in range(sub_d_length - 1, -1, -1):
        temp = sub_d[sub_d_length - 1]
        for k in range(0, sub_d_length - 1 - j):
            temp = sub_d[sub_d_length - 2 - k] + '.' + temp
            
        if temp in sub_domain:
            sub_domain[temp] += int(times_count)
        else:
            sub_domain[temp] = int(times_count)
        
return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]
        
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count2.py)

```python
sub_domain = {}
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)

    temp = ""
    for subs_d in domain.split('.')[::-1]:
        temp = subs_d + temp
        if temp in sub_domain:
            sub_domain[temp] += int(times_count)
        else:
            sub_domain[temp] = int(times_count)
        temp = '.' + temp

        
return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]

```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count3.py)

```python
sub_domain = collections.Counter()
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)
    frags = domain.split('.')

    for i in range(len(frags)):
        sub_domain['.'.join(frags[i:])] += int(times_count)

        
return [ "{0} {1}".format(v, k) for k, v in sub_domain.items() ]

```
