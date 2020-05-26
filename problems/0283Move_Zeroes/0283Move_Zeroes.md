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

找0, remove, del or pop, then append(0)

**Approach 2:** 

找两个pointer, slow and fast, slow pointer 不是0 就替换

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0283Move_Zeroes/0283Move_Zeroes1.py)

```python
i = 0
length = len(nums)
while i < length:
    if nums[i] == 0:
        del nums[i]
        nums.append(0)
        length -= 1
    else:
        i += 1
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0283Move_Zeroes/0283Move_Zeroes2.py)

```python
slow, fast = 0, 0
length = len(nums)
for fast in range(length): 
    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
```
