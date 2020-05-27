## Climbing Stairs

### Problem Link
https://leetcode.com/problems/climbing-stairs/

### Problem Description 

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given n will be a positive integer.

```
Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

```
Example 2: 

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

### How to solve 

**Approach 1:** 

Use dictionary to map every roman character to int number, and checking the size of current number with the next one 

**Approach 2:** 

Use dictionary to map every roman character to int number. 

**Approach 3:** 

根据当前值与下一个值的大小，做加法或减法

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0013Roman_to_Integer/0013Roman_to_Integer1.py)

```python
roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

sum_int = 0
i = 0
while i < (len(s) - 1):
    if roman_dict[s[i]] < roman_dict[s[i + 1]]:
        sum_int += roman_dict[s[i + 1]] - roman_dict[s[i]]
        i += 2
    else:
        sum_int += roman_dict[s[i]]
        i += 1
if i != len(s):
    sum_int += roman_dict[s[-1]]

return sum_int
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0013Roman_to_Integer/0013Roman_to_Integer2.py)

```python
roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, 
                "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}

sum_int = 0
i = 0
while i < (len(s) - 1):
    if s[i : i + 2] in roman_dict:
        sum_int += roman_dict[s[i : i + 2]]
        i += 2
    else:
        sum_int += roman_dict[s[i]]
        i += 1
if i != len(s):
    sum_int += roman_dict[s[-1]]

return sum_int
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0013Roman_to_Integer/0013Roman_to_Integer3.py)

```python
roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

sum_int = 0
i = 0
for i in range(len(s) - 1):
    if roman_dict[s[i]] < roman_dict[s[i + 1]]:
        sum_int -= roman_dict[s[i]]
    else:
        sum_int += roman_dict[s[i]]
sum_int += roman_dict[s[-1]]

return sum_int
```