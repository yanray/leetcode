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

**Approach 2:** 

Linear time solution, 遍历, 记录次数, 查次数, 找对应的index

**Approach 3:** 

OrderDict

**Approach 4:** 

Dict.get()


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


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0387First_Unique_Character_in_a_String/0387First_Unique_Character_in_a_String2.py)

```python
"""
:type s: str
:rtype: int
"""
# build hash map : character and how often it appears
count = collections.Counter(s)

# find the index
for idx, ch in enumerate(s):
    if count[ch] == 1:
        return idx     
return -1
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0387First_Unique_Character_in_a_String/0387First_Unique_Character_in_a_String3.py)

```python
# Explaination: Ordered Dict will save the characters it encounters in
# same sequence as the original string. Hence it becomes easy to catch hold of the first
#unique character. Then according to the counter variable, whenever the first 1 is encountered
# the corresponding dict.key's index is returned from the original String.
    for i,j in collections.OrderedDict(collections.Counter(s)).items():
        if j == 1:
            return s.index(i)
    return -1
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0387First_Unique_Character_in_a_String/0387First_Unique_Character_in_a_String4.py)

```python
counts = dict()

for char in s:
counts[char] = counts.get(char, 0) + 1

for i in range(0, len(s)):        
if counts[s[i]] == 1:
    return i

return -1
```

