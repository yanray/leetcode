## First Bad Version

### Problem Link

https://leetcode.com/problems/first-bad-version/

### Problem Description 

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

```
Example 1: 

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

```


### How to solve 

**Approach 1:** 

二分法, 找到 i 为 false, i + 1 为True 即 return 

**Approach 2:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0278First_Bad_Version/0278First_Bad_Version1.py)

```python
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        last_false = 0
        first_true = n
        
        left = 1 
        right = n
        while last_false + 1 != first_true:
            test_val = (left + right) // 2
            if isBadVersion(test_val):
                right = test_val
                first_true = test_val
            else:
                left = test_val
                last_false = test_val
            
        return first_true
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0278First_Bad_Version/0278First_Bad_Version2.py)

```python

```

