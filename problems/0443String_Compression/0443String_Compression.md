## String Compression

### Problem Link
https://leetcode.com/problems/string-compression/

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
if not s:
    return True

num_al = []
for ch in s:
    if ch.isdigit():
        num_al.append(ch)
    elif ch.islower():
        num_al.append(ch)
    elif ch.isupper():
        num_al.append(ch.lower())
        
return num_al == num_al[::-1]
```




[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0125Valid_Palindrome/0125Valid_Palindrome2.py)

```python
if not s:
    return True

num_al = []
for ch in s:
    if ch.isdigit():
        num_al.append(ch)
    elif ch.islower():
        num_al.append(ch)
    elif ch.isupper():
        num_al.append(ch.lower())
        
return num_al == num_al[::-1]
```