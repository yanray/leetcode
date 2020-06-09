## ZigZag Conversion

### Problem Link

https://leetcode.com/problems/zigzag-conversion/

### Problem Description 

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```

P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

```
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

```

```
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

```

### How to solve 

**Approach 1:** 

根据ZigZag的规律逐行查找Index的值

**Approach 2:** 

Visit by Row:

* Characters in row 00 are located at indexes k \; (2 \cdot \text{numRows} - 2)k(2⋅numRows−2)
* Characters in row \text{numRows}-1numRows−1 are located at indexes k \; (2 \cdot \text{numRows} - 2) + \text{numRows} - 1k(2⋅numRows−2)+numRows−1
* Characters in inner row ii are located at indexes k \; (2 \cdot \text{numRows}-2)+ik(2⋅numRows−2)+i and (k+1)(2 \cdot \text{numRows}-2)- i(k+1)(2⋅numRows−2)−i.


**Approach 3 - 4:** 

先对每行排序, 最终结合



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0006ZigZag_Conversion/0006ZigZag_Conversion1.py)

```python
if numRows == 1:
    return s

new_s = ""

length_s = len(s)
index = 0
curr_row = 1
compare_row = 1
for i in range(length_s):
    new_s += s[index]
    if curr_row == 1 or curr_row == numRows:
        index += 2 * (numRows - curr_row) + 2 * (curr_row - 1)
    # elif curr_row == numRows:
        # index += 2 * (curr_row - 1)
    else:
        index += 2 * abs(compare_row - curr_row)
        if compare_row == numRows:
            compare_row = 1
        else:
            compare_row = numRows
    if index >= length_s:
        curr_row += 1
        compare_row = numRows
        index = curr_row - 1
        
return new_s
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0006ZigZag_Conversion/0006ZigZag_Conversion2.py)

```python
if numRows == 1:
    return s 
n = len(s)
cycle = 2*numRows - 2
strlist = []
for i in range(numRows):
    for j in range(i, n, cycle):
        strlist.append(s[j])
        if i != numRows-1 and i != 0 and j+cycle-2*i < n:
            strlist.append(s[j+cycle-2*i])             
newstr = ''.join(strlist)
return newstr
```

[Approach 3](fast)(https://github.com/yanray/leetcode/blob/master/medium/0006ZigZag_Conversion/0006ZigZag_Conversion3.py)

```python
curr_row = 0
direction = 1
outp = [""] * numRows
for i in range(len(s)):
    outp[curr_row] += s[i]
    if numRows > 1:
        curr_row += direction
        if curr_row == 0 or curr_row == numRows -1:
            direction *= -1
outputStr = ""
for j in range(numRows):
    outputStr += outp[j]
return outputStr
```

[Approach 4](fast)(https://github.com/yanray/leetcode/blob/master/medium/0006ZigZag_Conversion/0006ZigZag_Conversion4.py)

```python
if numRows == 1 or numRows > len(s):  # corner case
    return s
res, i, step = ['' for r in range(numRows)], 0, 0  # a string for each line
for ch in s:
    res[i] += ch
    if i == 0:  # first row
        step = 1  # down
    if i == numRows - 1:  # last row
        step = -1  # up
    i += step
return "".join(res)
```