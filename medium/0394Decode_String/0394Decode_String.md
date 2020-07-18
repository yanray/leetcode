## Decode String

### Problem Link

https://leetcode.com/problems/decode-string/

### Problem Description 

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

```
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

```

```
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

```

```
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

```

```
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

```


### Code (python)

[Approach 1] (%) 

```python
class Solution:
    def decodeString(self, s: str) -> str:
            
        
        stack = []
        curr_str = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if curr_str != "":
                    stack.append(curr_str)
                    curr_str = ""
                
                temp = s[i]
                i += 1
                while s[i].isdigit():
                    temp += s[i]
                    i += 1
                stack.append(temp)
                i -= 1
                
            elif s[i] == "[":
                i += 1
                continue
            elif s[i] == "]":
                while stack[-1].isalpha():
                    curr_str = stack.pop() + curr_str
                stack.append(int(stack.pop()) * curr_str)
                curr_str = ""
            else:
                curr_str += s[i]
                
            i += 1
                    
        return "".join(stack) + curr_str
```