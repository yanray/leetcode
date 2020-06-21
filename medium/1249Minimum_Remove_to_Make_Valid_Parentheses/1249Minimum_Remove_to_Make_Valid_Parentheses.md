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

[Approach 2] (50 - 65%)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)

```

[Approach 3] (50 - 65%)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        s = delete_invalid_closing(s, "(", ")")
        print(s)
        
        s = delete_invalid_closing(s[::-1], ")", "(")
        print(s)
        return s[::-1]
```

[Approach 4] (50 - 65%)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Parse 1: Remove all invalid ")"
        first_parse_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_parse_chars.append(c)

        # Parse 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for c in first_parse_chars:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(c)

        return "".join(result)
```

Optimization of approach 4

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # Parse 1: Remove all invalid ")"
        first_parse_chars = []
        balance = 0
        open_seen = 0
        close_seen = 0
        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            if c == ")":
                close_seen += 1
                if balance == 0:
                    close_seen -= 1
                    continue
                balance -= 1
            first_parse_chars.append(c)

        # Parse 2: Remove the rightmost "("
        
        open_to_keep = open_seen - close_seen
        for i in range(len(first_parse_chars) - 1, -1, -1):
            if first_parse_chars[i] == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    break
                first_parse_chars.pop(i)
                    
        return "".join(first_parse_chars)
```


