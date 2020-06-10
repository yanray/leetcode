## Longest Palindromic Substring

### Problem Link

https://leetcode.com/problems/longest-palindromic-substring/

### Problem Description 

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```
Example 1: 

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

```

```
Example 2: 

Input: "cbbd"
Output: "bb"

```

### How to solve 

**Approach 1:** 

Expand Around Center

**Approach 2:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0005Longest_Palindromic_Substring/0005Longest_Palindromic_Substring1.py)

```python
maxPal = ''
for i in range(len(s)):
    maxPal = max(maxPal, self.largestPalindrome(s, i-1, i), self.largestPalindrome(s,i-1,i+1), key=len)
return maxPal

def largestPalindrome(self, s, i, j):
while i >= 0 and j < len(s):
    if s[i] != s[j]:
        break
    i -= 1
    j += 1
return s[i+1:j]
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0005Longest_Palindromic_Substring/0005Longest_Palindromic_Substring2.py)

```python

```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0005Longest_Palindromic_Substring/0005Longest_Palindromic_Substring2.py)

```python

```

