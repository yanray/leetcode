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

把words里的字母按照order里面的顺序替换成正常顺序 所对应的new words, 然后比较大小判断顺序

**Approach 2:** 

根据order创建一个hashmap，根据hashmap对应的顺序对words进行重新排序，看words是否等于排序后的words

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary1.py)

```python
right_order = 'abcdefghijklmnopqrstuvwxyz'

trans = str.maketrans(order, right_order)
new_words = [w.translate(trans) for w in words]

for i in range(len(new_words) - 1): 
    if new_words[i] > new_words[i + 1]:
        return False

return True    
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary2.py)

```python
hashmap = {c:i for i, c in enumerate(order)}
return words == sorted(words, key = lambda w: [hashmap[x] for x in w])
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary3.py)

```python
return words == sorted(words, key = lambda w: [order.index(x) for x in w])
```