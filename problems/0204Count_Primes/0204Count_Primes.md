## Count Primes

### Problem Link
https://leetcode.com/problems/count-primes/

### Problem Description 

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
**Follow up:**
Could you solve it using only O(1) extra space?

```
Example 1: 

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

```

```
Example 2: 

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

```

```
Example 3: 

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

```

### How to solve 

**Approach 1:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome1.py)

```python
anchor = write = 0
for read, c in enumerate(chars):
    if read + 1 == len(chars) or chars[read + 1] != c:
        chars[write] = chars[anchor]
        write += 1
        if read > anchor:
            for digit in str(read - anchor + 1):
                chars[write] = digit
                write += 1
        anchor = read + 1
return write
```




[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome2.py)

```python
if len(chars) == 1:
    return 1

count_ch = 1
pointer = 0
for i in range(len(chars) - 1):
    if (i + 2) == len(chars) and chars[i + 1] == chars[pointer]:
        pointer += 1
        for digit in str(count_ch + 1):
            chars[pointer] = digit
            pointer += 1
    elif (i + 2) == len(chars) and chars[i + 1] != chars[pointer]:
        pointer += 1
        if count_ch != 1:
            chars[pointer] = str(count_ch)
            chars[pointer + 1] = chars[i + 1]
            pointer += 2
        else:
            chars[pointer] = chars[i + 1]
            pointer += 1
    elif chars[i] == chars[pointer] and chars[i + 1] == chars[pointer]:
        count_ch += 1
    elif chars[i] == chars[pointer] and chars[i + 1] != chars[pointer]:
        if count_ch == 1:
            chars[pointer + 1] = chars[i + 1]
            pointer += 1
        else:
            pointer += 1
            for digit in str(count_ch):
                chars[pointer] = digit
                pointer += 1
            chars[pointer] = chars[i + 1]
            count_ch = 1


return len(chars[:pointer])
```