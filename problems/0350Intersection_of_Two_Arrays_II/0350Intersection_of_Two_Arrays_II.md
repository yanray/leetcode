## Strobogrammatic Number

### Problem Link

https://leetcode.com/problems/strobogrammatic-number/

### Problem Description 

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

```
Example 1:

Input: num = "69"
Output: true

```

```
Example 2:

Input: num = "88"
Output: true

```

```
Example 3:

Input: num = "962"
Output: false

```

```
Example 4:

Input: num = "1"
Output: true

```


### Code (python)

[Approach 1] (93%)

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        hash_dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        
        for i in range(len(num) // 2 + 1):
            if num[i] in hash_dict:
                if hash_dict[num[i]] != num[~i]:
                    return False
            else:
                return False
            
        return True
```

[Approach 2] (93%)

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotates = {"0": "0", "1": "1", "8": "8", "6": "9",  "9": "6"} 
        return all(b in rotates and rotates[b] == a for a, b in zip(num, num[::-1]))
```