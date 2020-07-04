## Backspace String Compare

### Problem Link

https://leetcode.com/problems/backspace-string-compare/

### Problem Description 

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

```
Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

```

```
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

```

```
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

```

```
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

```

**Note:**

* 1 <= S.length <= 200
* 1 <= T.length <= 200
* S and T only contain lowercase letters and '#' characters.

**Follow up:**

* Can you solve it in O(N) time and O(1) space?


### Code (python)

[Approach 1: Build String] (85%)

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def build_str(s):
            new_s = []
            for ch in s:
                if ch != "#":
                    new_s.append(ch)
                elif new_s:
                    new_s.pop()
                    
            return new_s
        
        return build_str(S) == build_str(T)
```

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(S: str) -> str:
            str_s = ''
            for i in range(len(S)):
                if S[i] != '#':
                    str_s += S[i]
                else:
                    str_s = str_s[:-1]
            return str_s
        return get_str(S) == get_str(T)
```


[Approach 2: Two Pointers] (85%) (only for python)

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```