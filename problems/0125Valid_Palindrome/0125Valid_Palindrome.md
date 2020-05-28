## Valid Palindrome

### Problem Link
https://leetcode.com/problems/valid-palindrome/

### Problem Description 

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

```
Example 1: 

Input: "A man, a plan, a canal: Panama"
Output: true

```

```
Example 2: 

Input: "race a car"
Output: false

```

### How to solve 

**Approach 1:** 

判断数字, 判断小写字母, 判断大写字母, 判断Palindrome

**Approach 2:** 

Two pointers, 头尾相比较


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome1.py)

```python
if not s:
    return True

num_al = []
for ch in s:
    if ch.isdigit():
        num_al.append(ch)
    elif ch.islower():
        num_al.append(ch)
    elif ch.isupper():
        num_al.append(ch.lower())
        
return num_al == num_al[::-1]
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome2.py)

```python
filtered_chars = filter(lambda ch: ch.isalnum(), s)
lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

filtered_chars_list = list(lowercase_filtered_chars)

return filtered_chars_list == filtered_chars_list[::-1]
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome3.py)

```python
i, j = 0, len(s) - 1

while i < j:
    while i < j and not s[i].isalnum():
        i += 1
    while i < j and not s[j].isalnum():
        j -= 1

    if i < j and s[i].lower() != s[j].lower():
        return False

    i += 1
    j -= 1

return True
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome4.py)

```python
s = s.lower()
s = [char for char in s if char.isalnum()]
return s == s[::-1]
```
