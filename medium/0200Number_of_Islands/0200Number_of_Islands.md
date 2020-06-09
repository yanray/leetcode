## Number of Islands

### Problem Link

https://leetcode.com/problems/number-of-islands/

### Problem Description 

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
Example 1: 

Input:
11110
11010
11000
00000

Output: 1

```

```
Example 2: 

Input:
11000
11000
00100
00011

Output: 3

```

### How to solve 

**Approach 1:** 




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium_hard/0003Longest_Substring_Without_Repeating_Characters/0003Longest_Substring_Without_Repeating_Characters1.py)

```python
if not s:
    return 0

sub_str_dict = {}
sub_len = [1]
sub_str_dict[s[0]] = 0

for i in range(1, len(s)):
    if s[i] in sub_str_dict:
        sub_len.append(min(i - sub_str_dict[s[i]], sub_len[i - 1] + 1))
        sub_str_dict[s[i]] = i
    else:
        sub_str_dict[s[i]] = i
        sub_len.append(sub_len[i - 1] + 1)

return max(sub_len)
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/medium_hard/0003Longest_Substring_Without_Repeating_Characters/0003Longest_Substring_Without_Repeating_Characters2.py)

```python
str_list = []
max_length = 0

for x in s:
    if x in str_list:
        str_list = str_list[str_list.index(x)+1:]
        
    str_list.append(x)    
    max_length = max(max_length, len(str_list))
    
return max_length
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/medium_hard/0003Longest_Substring_Without_Repeating_Characters/0003Longest_Substring_Without_Repeating_Characters3.py)

```python
l,r,m,d=0,0,0,set()
while r < len(s):
    if not s[r] in d:
        d.add(s[r])
        m = max(len(d),m)
        r += 1
    else:
        d.remove(s[l])
        l += 1
return m
```

[Approach 4](https://github.com/yanray/leetcode/blob/master/medium_hard/0003Longest_Substring_Without_Repeating_Characters/0003Longest_Substring_Without_Repeating_Characters4.py)

```python
str_dict = {}
start, max_len = 0, 0
for i in range(len(s)):
    if s[i] in str_dict:
        start = max(str_dict[s[i]], start)
    max_len = max(max_len, i - start + 1)
    str_dict[s[i]] = i + 1
return max_len
```
