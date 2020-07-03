## Excel Sheet Column Title

### Problem Link

https://leetcode.com/problems/excel-sheet-column-title/

### Problem Description 

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```

```
Example 1:

Input: 1
Output: "A"

```

```
Example 2:

Input: 28
Output: "AB"

```

```
Example 3:

Input: 701
Output: "ZY"

```

```
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

```

### Code (python)

[Approach 1] (91%)

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        
        title = ""
        while n > 26:
            n, mod = n // 26, n % 26
            if mod != 0:
                title = chr(mod + 64) + title
            else:
                n -= 1
                title = "Z" + title

        title = chr(n + 64) + title
        
        return title
```

[Approach 2] (74%)

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alen = len(alphabet)
        base = ''

        while n > 0 :
            n -= 1
            n, j = divmod(n, alen)
            base += alphabet[j] # + base

        return base[::-1]
```

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        column = ''
        while n:
            n -= 1
            column += chr(n % 26 + 65)
            n //= 26
        return column[::-1]
```