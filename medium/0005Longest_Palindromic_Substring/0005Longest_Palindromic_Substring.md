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
       res, max_len, n= '', 0, len(s)
        dp = [[0]*n for _ in range(n)]

        print(dp)
        for i in range(n):
            dp[i][i] = 1
            res = s[i]
            max_len = 1

        print(dp)
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res = s[i:i+2]
                max_len = 2

        print(dp)
        for i in range(n):
            for j in range(i-1):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = 1
                    if i-j+1>max_len:
                        max_len = i-j+1
                        res = s[j:i+1]
        return res
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0005Longest_Palindromic_Substring/0005Longest_Palindromic_Substring2.py)

```python

```

