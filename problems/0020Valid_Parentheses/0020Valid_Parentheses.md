## Valid Parentheses

### Problem Link
https://leetcode.com/problems/valid-parentheses/

### Problem Description 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

```
Example1:

Input: "()"
Output: true

```

```
Example2:

Input: "()[]{}"
Output: true

```

```
Example3:

Input: "(]"
Output: false

```

```
Example4:

Input: "([)]"
Output: false

```

```
Example5:

Input: "{[]}"
Output: true

```

### How to solve 
创建一个Stack, 遍历输入的string, 如果是左括号就push到Stack, 如果是右括号就在Stack里pop一个值出来，看是否有相应的左括号，直到结束

Better Solution: 不停的查询 '()', '[]', '{}', 并替换成'', 如果最终输入的string成为了empty string, 就是true, else false. 


### Code (python)

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum1.py)

```python
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in nums:
        if i != nums.index(diff):
            return [i, nums.index(diff)]
```

[Good Solution 1](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum2.py)

```python
h = {}
for i, num in enumerate(nums):
    n = target - num
    if n not in h:
        h[num] = i
    else:
        return [h[n], i]
```

[Good Solution 2](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum3.py)

```python
hashtable = {};
for i in range(len(nums)):
    if nums[i] not in hashtable:
        hashtable[target-(nums[i])] = i;
    else:
        return [hashtable[nums[i]], i];
```