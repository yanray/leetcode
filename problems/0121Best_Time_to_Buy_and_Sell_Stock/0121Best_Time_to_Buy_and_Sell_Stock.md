## Best Time to Buy and Sell Stock

### Problem Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Problem Description 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.


```
Example1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

```

```
Example2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

```


### How to solve 

**Method 1:** 




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

[Method 2](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files2.py)

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

[Method 3](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files3.py)
```python
def sortfunc(x):
    identifier, rest = x.split(' ', 1)
    return(0, rest, identifier) if rest[0].isalpha() else (1, )
    
logs.sort(key = sortfunc)
return logs
```