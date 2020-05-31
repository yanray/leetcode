## Valid Anagram

### Problem Link

https://leetcode.com/problems/valid-anagram/

### Problem Description 

Given two strings s and t , write a function to determine if t is an anagram of s.

```
Example 1: 

Input: s = "anagram", t = "nagaram"
Output: true

```

```
Example 2: 

Input: s = "rat", t = "car"
Output: false

```

**Note:**

You may assume the string contains only lowercase alphabets.

**Follow up:**

What if the inputs contain unicode characters? How would you adapt your solution to such case?

### How to solve 

**Approach 1:** 

Use collections.Counter() to check if equal 

**Approach 1:** 

Sort

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0242Valid_Anagram/0242Valid_Anagram1.py)

```python
return collections.Counter(s) == collections.Counter(t)
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0242Valid_Anagram/0242Valid_Anagram2.py)

```python
return sorted(s) == sorted(t)
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0242Valid_Anagram/0242Valid_Anagram3.py)

```python
char_count = {}
for char in s: 
    char_count[char] = char_count.get(char, 0) + 1
for char in t:
    char_count[char] = char_count.get(char, 0) - 1
return False not in [char_count[char] == 0 for char in char_count]
```

