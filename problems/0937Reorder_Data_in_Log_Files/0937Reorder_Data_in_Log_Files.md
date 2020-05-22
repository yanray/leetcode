## Reorder Data in Log Files

### Problem Link
https://leetcode.com/problems/reorder-data-in-log-files/

### Problem Description 

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.


```
Example:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

```


### How to solve 

**Method 1:** 

先分离digit-logs, 排序好放在一个新的list, 对剩下的letters-log排序, 然后提取出第一个' '以后的内容进行排序, 再根据dictionary对应的value排序好letters-log.

**Method 2:**



**Method 3:**

nums[i] = max(nums[i], nums[i] + num[i - 1])
​

### Code (python)

[Method 1]

```python

```

[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0053Maximum_Subarray/0053Maximum%20Subarray2.py)

```python
max_sum = nums[0]
local_max_sum = nums[0]
for i in range(1, len(nums)):
    local_max_sum = max(nums[i], local_max_sum + nums[i])
    max_sum = max(max_sum, local_max_sum)
    
return max_sum
```

[Method 3](https://github.com/yanray/leetcode/blob/master/problems/0053Maximum_Subarray/0053Maximum%20Subarray3.py)

```python
max_sum = nums[0]
for i in range(1, len(nums)):
    if(nums[i - 1] >= 0):
        nums[i] += nums[i - 1]
    max_sum = max(nums[i], max_sum)
    
return max_sum
```

[Method 4](https://github.com/yanray/leetcode/blob/master/problems/0053Maximum_Subarray/0053Maximum%20Subarray4.py)
```python
for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i-1]+nums[i])
    
return max(nums)
```