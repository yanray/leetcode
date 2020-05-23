## Verifying an Alien Dictionary

### Problem Link
https://leetcode.com/problems/verifying-an-alien-dictionary/

### Problem Description 

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


```
Example1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

```


```
Example2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

```
Example3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character.

```

### How to solve 

**Approach 1:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0937Reorder_Data_in_Log_Files/0937Reorder_Data_in_Log_Files1.py)

```python

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