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

[Approach 1] (95%)

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
            elif list_s[i] == ")":
                if len(l_index) == 0:
                    delete_index.append(i)
                else:
                    l_index.pop()
                    
        delete_index += l_index
        for index in delete_index:
            list_s[index] = ""
                
        return "".join(list_s)
```

(95%)

```python
def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)
```

(85%)
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        i,n=0,len(s)
        
        while i<n:
            if s[i]=="(":
                stack.append(i)
            if s[i]==")":
                if not stack:
                    s=s[:i]+s[i+1:]
                    n-=1
                    continue
                else:
                    stack.pop()       
            i+=1
            
            
        if stack:
            while stack:
                idx=stack.pop()
                s=s[:idx]+s[idx+1:]
                
        return s
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


[Approach 4] (80% around)

```python
class Solution:
    def minRemoveToMakeValid(self, a: str) -> str:
        def invalidIndexes(a):
            '''
            Helper. Returns indexes of the invalid parentheses
            '''
            # balance represents how many open '(' vs closed ')' parentheses we've seen so far
            # Zero balance means that we've seen equal number '(' and ')'.
            # Negative balance means that we've seen more ')' than '('. 
            # Positive balance means that we've seen more '(' than ')'.
            # If at any point of processing we got negative balance, we immediatly can mark current ')' as invalid.
            
            balance = 0
            for i, c in enumerate(a):
                if c == '(':
                    # increase balance on '('
                    balance += 1
                elif c == ')':
                    # found ')', we are about to decrese balance,
                    # are we balanced already?
                    if balance == 0:
                        # we are balanced, thus ')' is not allowed (otherwise balance goes negative)
                        # yield an index of the invalid parenthesis
                        yield i
                    else:
                        # decrease balance on ')'
                        balance -= 1

            # is balance positive?
            if balance > 0:
                # positive balance means that the string contains extra "(" chars
                # rightmost "(" chars are those extra, lets yield them as invalid
                # until we got balanced state (balance = 0)

                # go over chars backwards
                for i in range(len(a) - 1, -1, -1):
                    c = a[i]
                    if c == '(':
                        # extra '(' found, yield it and decrease balance
                        yield i
                        balance -= 1

                        # are we balanced now?
                        if balance == 0:
                            return

        # init result as array of input characters
        res = list(a)

        # for each invalid character index
        for i in invalidIndexes(a):
            # replace i-th result character with None marker
            # i.e. mark it as invalid
            res[i] = None

        # transform result into required type and presentation: string w/o None characters
        # remove None characters (they are all invalid)
        res = filter(lambda el: el is not None, res)
        # array to string
        return ''.join(res)
```

[Approach 5] (99% around)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        open = 0
        s = list(s)
        
        for i, c in enumerate(s):
            if c == '(': 
                open += 1
            elif c == ')':
                if not open: 
                    s[i] = ""
                else: 
                    open -= 1
        
        for i in range(len(s)-1, -1, -1):
            if not open: 
                break
            if s[i] == '(': 
                s[i] = ""
                open -= 1
        
        return "".join(s)
```