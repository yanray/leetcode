## Excel Sheet Column Number

### Problem Link

https://leetcode.com/problems/excel-sheet-column-number/

### Problem Description 

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

```
Example 1:

Input: "A"
Output: 1

```

```
Example 2:

Input: "AB"
Output: 28

```

```
Example 3:

Input: "ZY"
Output: 701

```
 
**Constraints:**

1. 1 <= s.length <= 7
2. s consists only of uppercase English letters.
3. s is between "A" and "FXSHRXW".


### Code (python)

[Approach 1] (23%) 

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        
        sum_val = 0
        carry = len(s) - 1
        base = 64
        for i in range(len(s)):
            sum_val += (ord(s[i]) - base) * (26 ** carry)
            carry -= 1
            
        return sum_val
```