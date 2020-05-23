## Add Strings

### Problem Link
https://leetcode.com/problems/add-strings/

### Problem Description 

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

```
Note:

1. The length of both num1 and num2 is < 5100.
2. Both num1 and num2 contains only digits 0-9.
3. Both num1 and num2 does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
```

### How to solve 

**Approach 1:** 

转成ascii, 转int, 相加

**Approach 2:** 

Using a dictionary to map "0": 0, "1": 1 and so on. (slow)

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0415Add_Strings/0415Add_Strings1.py)

```python
int_num1 = 0
for i in range(len(num1)):
    temp = ord(num1[i]) - 48
    int_num1 = int_num1 * 10 + temp

int_num2 = 0
for i in range(len(num2)):
    temp = ord(num2[i]) - 48
    int_num2 = int_num2 * 10 + temp
    
return str(int_num1 + int_num2)
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0415Add_Strings/0415Add_Strings2.py)

```python
int_num1 = 0
for i in range(len(num1)):
    int_num1 = int_num1 * 10 + ord(num1[i]) - ord('0')
    
int_num2 = 0
for i in range(len(num2)):
    int_num2 = int_num2 * 10 + ord(num2[i]) - ord('0')
    
return str(int_num1 + int_num2)
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0415Add_Strings/0415Add_Strings3.py)

```python
str_to_int_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

int_num1 = 0
len_num1 = len(num1)
for i in range(len_num1):
    int_num1 += 10 ** (len_num1 -1 - i) * str_to_int_dict[num1[i]]
    
int_num2 = 0
len_num2 = len(num2)
for i in range(len_num2):
    int_num2 += 10 ** (len_num2 -1 - i) * str_to_int_dict[num2[i]]
    
return str(int_num1 + int_num2)
```