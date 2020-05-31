## First Unique Character in a String

### Problem Link

https://leetcode.com/problems/first-unique-character-in-a-string/

### Problem Description 

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

```
Example 1: 

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

```

**Note:** You may assume the string contain only lowercase letters.

### How to solve 

**Approach 1:** 

遍历, 如果出现一次, 就在dictionary 里标记 index, 如果more than once, mark as -1

**Approach 1:** 

Linear time solution, 遍历, 记录次数, 查次数, 找对应的index


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0387First_Unique_Character_in_a_String/0387First_Unique_Character_in_a_String1.py)

```python
see_once = {}
for i, ch in enumerate(s):
    if ch in see_once:
        see_once[ch] = -1
    else:
        see_once[ch] = i

for v in see_once.values():
    if v != -1:
        return v
        
return -1
```


