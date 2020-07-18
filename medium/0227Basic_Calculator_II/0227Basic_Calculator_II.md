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

[Approach 2: Same Solution for 3 poblems Basic Calculator I, II, III] (25%)

```python
class Solution:
    def calculate(self, s: str) -> int:
        ## RC ##
        ## APPROACH : 2 STACKS ##
        ## Similar to Leetcode: 772. Basic Calculator ##
        ## Similar to Leetcode: 224. Basic Calculator ##
        
        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##
                
        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":  # integer division
                return first // second
        
        def precedence(current_op, op_from_ops):
            if( op_from_ops == "(" or op_from_ops == ")" ):
                return False
            if(current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True     # when curr = "+", top of ops = "*" or "/"
        
        if not s: return 0
        N = len(s)
        nums = [] if(s[0] !='-') else [0]                                       # edge case -1 + 2/3
        ops = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = c
                while i < N - 1 and s[i + 1].isdigit():                    # more than 1 digit numbers
                    num += s[i + 1]
                    i += 1
                nums.append(int(num))
            elif c == "(":
                ops.append(c)
                if( i+1 < N and s[i+1] == '-'): 
                    nums.append(0)                                              # "1 - (-7)" edge case.
            elif c == ")":
                while ops[-1] != "(":                                           # do the math when we encounter a ')' until '('
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()                                                       # watch out, popping open brace '('
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[-1]):                 # check for precedence order and make calculations, APPEND RESULT TO NUMS STACK EVERY TIME.
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))   
                ops.append(c)                                                   # append to operators stack
            i += 1                                                              # basic while loop increment
        
        while len(ops) > 0:                                                     # finally we perform calculations till stack is empty.
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            
        return nums.pop()
```

[Approach 3] (93%)

```python
class Solution:
    def calculate(self, s: str) -> int:
        num, presign, stack=0, "+", []
        for i in s+'+':
            if i.isdigit():
                num = num*10 +int(i)
            elif i in '+-*/':
                if presign =='+':
                    stack.append(num)
                if presign =='-':
                    stack.append(-num)
                if presign =='*':
                    stack.append(stack.pop()*num)
                if presign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                presign = i
                num = 0
                
        return sum(stack)
```

```python 
class Solution:
    def calculate(self, s: str) -> int:
        
        
        result = 0
        temp = 0
        num = 0
        
        
        current_symbol = '+'
        
        for idx, c in enumerate(s + '+'):
            
            if c in '+-/*':
                
                if current_symbol == '+':
                    result += temp
                    temp = num
                elif current_symbol == '-':
                    result += temp
                    temp = -num
                elif current_symbol == '*':
                    temp *= num
                elif current_symbol == '/':
                    temp = int(temp / num)
                    
                current_symbol = c
                num = 0
                
            elif c.isdigit():
                num = num * 10 + int(c)
                
        return result + temp
```