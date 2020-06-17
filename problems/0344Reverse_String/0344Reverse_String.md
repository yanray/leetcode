## Reverse String

### Problem Link

https://leetcode.com/problems/reverse-string/

### Problem Description 


Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

```
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

```
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

### How to solve 

**Approach 1:**

前后互换value

**Approach 2:**




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0344Reverse_String/0344Reverse_String1.py)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0344Reverse_String/0344Reverse_String2.py)

```python

```

