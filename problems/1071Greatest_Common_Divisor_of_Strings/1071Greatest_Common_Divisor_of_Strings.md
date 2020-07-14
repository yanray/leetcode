## Greatest Common Divisor of Strings

### Problem Link

https://leetcode.com/problems/greatest-common-divisor-of-strings/

### Problem Description 

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

```
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

```

```
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

```

```
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

```
 
**Note:**

1. 1 <= str1.length <= 1000
2. 1 <= str2.length <= 1000
3. str1[i] and str2[i] are English uppercase letters.


### Code (python)

[Approach 1] (84%) 

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if (str1 + str2) != (str2 + str1):
            return ""
        elif str1 == str2:
            return str1
        else:
            gcd_val = math.gcd(len(str1), len(str2))
            # return self.gcdOfStrings(str1[:gcd_val], str2[:gcd_val])
            return str1[:gcd_val]
```

[Approach 2] (50%) (fast) 

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            if str1 == str2: 
                return str2
            if len(str1) >= len(str2) and str2 in str1:
                i = str1.index(str2)
                return self.gcdOfStrings(str2, str1[:i]+str1[i+len(str2):])
            elif len(str1) < len(str2) and str1 in str2:
                i = str2.index(str1)
                return self.gcdOfStrings(str1, str2[:i]+str2[i+len(str1):])
            return '' 
```

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/426882/python-understandable-from-numerical-gcd

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/384620/Python-Solution-or-Euclid's-algorithm-or-10-lines-or-Time-Complexity-greater-95-or-Space-Complexity-greater-100