## Valid Parentheses

### Problem Link
https://leetcode.com/problems/valid-parentheses/

### Problem Description 

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

```
Example1:

Input: "()"
Output: true

```

```
Example2:

Input: "()[]{}"
Output: true

```

```
Example3:

Input: "(]"
Output: false

```

```
Example4:

Input: "([)]"
Output: false

```

```
Example5:

Input: "{[]}"
Output: true

```

### How to solve 
创建一个Stack, 遍历输入的string, 如果是左括号就push到Stack, 如果是右括号就在Stack里pop一个值出来，看是否有相应的左括号，直到结束

Better Solution: 不停的查询 '()', '[]', '{}', 并替换成'', 如果最终输入的string成为了empty string, 就是true, else false. 


### Code (python)

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0020Valid_Parentheses/0020Valid_Parentheses1.py)

```python
if len(s):
    parenthese_left = ['(', '{', '[']
    parenthese_right = [')', '}', ']']
    num_record = []
    for i in range(len(s)):
        if s[i] in parenthese_left:
            num_record.append(parenthese_left.index(s[i]))
        else:
            # print('position 2')
            if not len(num_record):
                return False
            elif(parenthese_right.index(s[i]) == num_record[len(num_record) - 1]):
                num_record.pop()
            else:
                return False
    if not len(num_record):
        return True
    else:
        return False
else:
    return True


```

[Good Solution 1](https://github.com/yanray/leetcode/blob/master/problems/0020Valid_Parentheses/0020Valid_Parentheses2.py)

```python
left = ['(', '{', '[']
right = [')', '}', ']']
Stack = []
for letter in s:
if letter in left:
    Stack.append(letter)
elif letter in right:
    if len(Stack) <= 0:
    return False
    if left.index(Stack.pop()) != right.index(letter):
        return False
return len(Stack) == 0

```

[Good Solution 2](https://github.com/yanray/leetcode/blob/master/problems/0020Valid_Parentheses/0020Valid_Parentheses3.py)

```python
while '()'in s or '{}' in s or '[]' in s:
    s = s.replace('()', '').replace('{}', '').replace('[]', '')
return s == ''
```