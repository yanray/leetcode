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

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary1.py)

```python
right_order = 'abcdefghijklmnopqrstuvwxyz'

trans = str.maketrans(order, right_order)
new_words = [w.translate(trans) for w in words]

for i in range(len(new_words) - 1): 
    if new_words[i] > new_words[i + 1]:
        return False

return True    
```
