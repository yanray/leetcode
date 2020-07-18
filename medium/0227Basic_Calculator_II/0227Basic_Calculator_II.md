## Basic Calculator II

### Problem Link

https://leetcode.com/problems/basic-calculator-ii/

### Problem Description 

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

```
Example 1:

Input: "3+2*2"
Output: 7

```

```
Example 2:

Input: " 3/2 "
Output: 1

```

```
Example 3:

Input: " 3+5 / 2 "
Output: 5

```

**Note:**

You may assume that the given expression is always valid.
Do not use the eval built-in library function.


### Code (python)

[Approach 1] (44%) 

```python
class Solution:
    def calculate(self, s: str) -> int:
        
        result = 0
        
        main_stack = []
        minor_stack = []
        curr_val = 0
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i] == "+" or s[i] == "-":
                minor_stack.append(curr_val)
                
                total = minor_stack[0]
                for j in range(1, len(minor_stack), 2):
                    if minor_stack[j] == "*":
                        total *= minor_stack[j + 1]
                    else:
                        total //= minor_stack[j + 1]
                main_stack.append(total)
                main_stack.append(s[i])
                curr_val = 0
                minor_stack = []

            elif s[i] == "*" or s[i] == "/":
                minor_stack.append(curr_val)
                minor_stack.append(s[i])
                curr_val = 0

            else:
                curr_val = curr_val * 10 + int(s[i])

        minor_stack.append(curr_val)
        # print("minor_stack", minor_stack)
        total = minor_stack[0]
        for j in range(1, len(minor_stack), 2):
            if minor_stack[j] == "*":
                total *= minor_stack[j + 1]
            else:
                total //= minor_stack[j + 1]
        main_stack.append(total)
            
        # print(main_stack)
        if main_stack:
            total = main_stack[0]
            for j in range(1, len(main_stack), 2):
                if main_stack[j] == "+":
                    total += main_stack[j + 1]
                else:
                    total -= main_stack[j + 1]
            return total
        else:
            return 0
```