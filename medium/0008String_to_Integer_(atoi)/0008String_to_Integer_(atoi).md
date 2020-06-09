## String to Integer (atoi)

### Problem Link

https://leetcode.com/problems/string-to-integer-atoi/

### Problem Description 

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**
* Only the space character ' ' is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

```
Example 1:

Input: "42"
Output: 42

```

```
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

```

```
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

```

```
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

```

```
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

```

### How to solve 

**Approach 1:** 




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0008String_to_Integer_(atoi)/0008String_to_Integer_(atoi)1.py)

```python
str = str.lstrip()

if not str:
    return 0

index = 0
INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

if str[index] == "-" and (index + 1) < len(str) and str[index + 1].isdigit():
    new_str = str[index] + str[index + 1]
    index += 2
    while index < len(str) and str[index].isdigit():
        new_str += str[index]
        index += 1

    return int(new_str) if int(new_str) >= INT_MIN else INT_MIN 

elif str[index] == "+" and (index + 1) < len(str) and str[index + 1].isdigit():
    new_str = str[index] + str[index + 1]
    index += 2
    while index < len(str) and str[index].isdigit():
        new_str += str[index]
        index += 1

    return int(new_str) if int(new_str) <= INT_MAX else INT_MAX

elif str[index].isdigit():
    new_str = str[index]
    index += 1
    while index < len(str) and str[index].isdigit():
        new_str += str[index]   
        index += 1
    return int(new_str) if int(new_str) <= INT_MAX else INT_MAX

else:
    return 0
```



[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0008String_to_Integer_(atoi)/0008String_to_Integer_(atoi)2.py)

```python
str = str.lstrip()

if not str:
    return 0

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

if str[0] == "+" or str[0] == "-":
    new_str = re.match("^\d+", str[1:])
    if new_str == None:
        return 0
    else:
        num = int(str[0] + new_str.group())
        if num >= 0:
            return num if num <= INT_MAX else INT_MAX
        else:
            return num if num >= INT_MIN else INT_MIN

if str[0].isdigit():
    new_str = re.match("^\d+", str)
    return int(new_str.group()) if int(new_str.group()) <= INT_MAX else INT_MAX

else:
    return 0
```





[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0008String_to_Integer_(atoi)/0008String_to_Integer_(atoi)1.py)

```python

```


[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0008String_to_Integer_(atoi)/0008String_to_Integer_(atoi)1.py)

```python

```


[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0008String_to_Integer_(atoi)/0008String_to_Integer_(atoi)1.py)

```python

```