## Reverse Words in a String III

### Problem Link

https://leetcode.com/problems/reverse-words-in-a-string-iii/

### Problem Description 

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

```
Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

```

**Note:** In the string, each word is separated by single space and there will not be any extra space in the string.

### Code (python)

[Approach 1] (98%)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        
        reversed_s = ""
        words = s.split(" ")
        for word in words:
            reversed_s += word[::-1] + " "

        return reversed_s[:len(reversed_s) - 1]
```

```python
return " ".join([i[::-1] for i in s.split()])
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x:x[::-1], s.split(' ')))
```

[Approach 2] (98%)

```python

```