## Longest Common Prefix

### Problem Link
https://leetcode.com/problems/longest-common-prefix/

### Problem Description 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


```
Example 1: 

Input: ["flower","flow","flight"]
Output: "fl"

```

```
Example 2: 

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

### How to solve 

**Approach 1:** 

Horizontal scanning, util the end of the List[string] or prefix == ""

**Approach 2:** 

Use hashmap, collections.Counter()

**Approach 3:** 

Use hashmap, collections.defaultdict(int)

**Approach 4:** 

Bit Manipulation

**Approach 5:** 

List Operation

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number1.py)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        else:
            prefix = strs[0]
            for s in strs:
                temp = prefix
                if temp == "":
                    return prefix
                else:
                    prefix = ""
                    for i in range(min(len(temp), len(s))):
                        if temp[i] == s[i]:
                            prefix += s[i]
                        else:
                            break

            return prefix
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number2.py)

```python
hashmap = collections.Counter(nums)

for n in nums:
    if hashmap[n] == 1:
        return n
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number3.py)

```python
hash_table = collections.defaultdict(int)
for i in nums:
    hash_table[i] += 1

for i in hash_table:
    if hash_table[i] == 1:
        return i
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number4.py)

```python
a = 0
for n in nums:
    a ^= n
    
return a
```


[Approach 5](https://github.com/yanray/leetcode/blob/master/problems/0136Single_Number/0136Single_Number5.py)

```python
no_duplicate_list = []
for i in nums:
    if i not in no_duplicate_list:
        no_duplicate_list.append(i)
    else:
        no_duplicate_list.remove(i)
return no_duplicate_list.pop()
```

