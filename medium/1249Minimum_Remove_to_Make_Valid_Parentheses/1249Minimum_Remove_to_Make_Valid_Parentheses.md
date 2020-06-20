## Minimum Remove to Make Valid Parentheses

### Problem Link

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

### Problem Description 

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as AB (A concatenated with B), where A and B are valid strings, or
* It can be written as (A), where A is a valid string.

```
Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

```

```
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

```

```
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

```

```
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

```

**Constraints:**

* 1 <= s.length <= 10^5
* s[i] is one of  '(' , ')' and lowercase English letters.

### Code (python)

[Approach 1] (65%)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        list_s = list(s)
        l_index = []
        r_index = []
        delete_index = []
        
        for i in range(len(list_s)):
            if list_s[i] == "(":
                l_index.append(i)
                
            if list_s[i] == ")":
                if len(l_index) == 0:
                    delete_index.append(i)
                else:
                    l_index.pop(-1)
                    
        delete_index += l_index
        for index in delete_index:
            list_s[index] = ""
                
        return "".join(list_s)
```