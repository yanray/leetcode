## Valid Palindrome II

### Problem Link
https://leetcode.com/problems/valid-palindrome-ii/

### Problem Description 

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

```
Example 1:

Input: "aba"
Output: True

```


```
Example 2: 

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

```

**Note:**

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

### How to solve 

**Approach 1:** 

判断此数是不是回文数，如果不是，依次比较头尾的字符，当字符不相等的时候，传子字符判断是不是回文数从而判定结果

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0680Valid_Palindrome_II/0680Valid_Palindrome_II1.py)

```python
def isPalindrome(s):
    return s == s[::-1]

if s == s[::-1]:
    return True

first, last = 0, len(s) - 1

while first < last:
    if s[first] != s[last]:
        return isPalindrome(s[first + 1 : last + 1]) or isPalindrome(s[first : last])
    first += 1
    last -= 1
    
return True
```
