## Reorder Data in Log Files

### Problem Link
https://leetcode.com/problems/reorder-data-in-log-files/

**Good Links:**

https://leetcode.com/problems/reorder-data-in-log-files/discuss/454259/937-reorder-data-in-log-files-py-all-in-one-by-talse

https://docs.python.org/3/howto/sorting.html

https://wiki.python.org/moin/HowTo/Sorting

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

**Approach 1:** 

先分离digit-logs, 排序好放在一个新的list, 对剩下的letters-log排序, 然后提取出第一个' '以后的内容进行排序, 再根据dictionary对应的value排序好letters-log.

**Approach 2:**

先分离digit-logs 和 letters-logs, 对letters-logs进行两次排序, 第一次根据第一个' '后的内容排序，第二次根据第一个' '前的内容排序

**Approach 3:**

Define 一个排序的function, 根据第一个' '把logs里的string分成两部分, identifier and rest, 如果rest[0]是字母, 先根据rest排序, 再根据identifier排序, 再排序digit-logs. 


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files1.py)

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

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files2.py)

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

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files3.py)
```python
def sortfunc(x):
    identifier, rest = x.split(' ', 1)
    return(0, rest, identifier) if rest[0].isalpha() else (1, )
    
logs.sort(key = sortfunc)
return logs
```