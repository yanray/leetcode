## Longest Substring Without Repeating Characters

### Problem Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Problem Description 

Given a string, find the length of the longest substring without repeating characters.

```
Example 1: 

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

```

```
Example 2: 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

```
Example 3: 

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

```
### How to solve 

**Approach 1:** 

sub_len[]用来保存长度, 类似于sliding window, 最终求max即可


**Approach 2:** 


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0003Longest_Substring_Without_Repeating_Characters/0003Longest_Substring_Without_Repeating_Characters1.py)

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
