## Reorder Data in Log Files

### Problem Link
https://leetcode.com/problems/reorder-data-in-log-files/

### Problem Description 

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.


```
Example:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

```


### How to solve 

**Method 1:** 

先分离digit-logs, 排序好放在一个新的list, 对剩下的letters-log排序, 然后提取出第一个' '以后的内容进行排序, 再根据dictionary对应的value排序好letters-log.

**Method 2:**



**Method 3:**

nums[i] = max(nums[i], nums[i] + num[i - 1])
​

### Code (python)

[Method 1](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files1.py)

```python
new_log = []
letters_dic = {}		
digit_log = []			
letters_log = []			

for i in range(0, len(logs)):
    for j in range(0, len(logs[i])):
        if logs[i][j] == ' ':
            if logs[i][j + 1].isdigit():
                digit_log.append(logs[i])
            else:
                letters_log.append(logs[i])
            break

letters_log.sort()
for i in range(0, len(letters_log)):
    for j in range(0, len(letters_log[i])):
        if letters_log[i][j] == ' ':
            letters_dic[i] = letters_log[i][j + 1 : len(letters_log[i])]
            break

letters_dic = sorted(letters_dic.items(), key = lambda x: x[1]) # (reverse = True)

for i in range(0, len(letters_dic)):
    num = letters_dic[i][0]
    new_log.append(letters_log[num])

new_log.extend(digit_log)

return new_log
```

[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0053Maximum_Subarray/0053Maximum%20Subarray3.py)

```python
digit_log = []
letters_log = []

for ll in logs:
    if ll[-1].isdigit():
        digit_log.append(ll)
    else:
        letters_log.append(ll)

letters_log.sort(key = lambda x: (x[x.index(' ') + 1: ], x[: x.index(' ') ]))

return letters_log + digit_log
```

[Method 3](https://github.com/yanray/leetcode/blob/master/problems/0053Maximum_Subarray/0053Maximum%20Subarray4.py)
```python
for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i-1]+nums[i])
    
return max(nums)
```