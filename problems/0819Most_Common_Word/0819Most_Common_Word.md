## Most Common Word

### Problem Link

https://leetcode.com/problems/most-common-word/

### Problem Description 

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

```
Example 1: 

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

```

Note:

* 1 <= paragraph.length <= 1000.
* 0 <= banned.length <= 100.
* 1 <= banned[i].length <= 10.
* The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
* paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
* There are no hyphens or hyphenated words.
* Words only consist of letters, never apostrophes or other punctuation symbols.

### How to solve 

**Approach 1:** 

use translate, split, collection.counter()

**Approach 2:** 

almost the same as approach 1


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0819Most_Common_Word/0819Most_Common_Word1.py)

```python
old_punc = string.punctuation
new_punc = ' ' * len(string.punctuation)
words = paragraph.translate(str.maketrans(old_punc, new_punc)).lower().split()

words_dict = collections.Counter(words)

for i in range(len(words_dict)):
    temp = words_dict.most_common(1)[0][0]
    if temp in banned:
        del words_dict[temp]
    else:
        return temp
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0819Most_Common_Word/0819Most_Common_Word2.py)

```python
banset = set(banned)
for c in "!?',;.":
    paragraph = paragraph.replace(c, " ")
count = collections.Counter(
    word for word in paragraph.lower().split())

ans, best = '', 0
for word in count:
    if count[word] > best and word not in banset:
        ans, best = word, count[word]

return ans
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0819Most_Common_Word/0819Most_Common_Word3.py)

```python
# convert to lower case and split string into words by spaces and punctuation
a = re.split(r'\W+', paragraph.lower())

# make new list consisitng of words not in banned list (remove banned words)
b = [w for w in a if w not in banned]

# return value that counted max times in the new list
return max(b, key = b.count)
```

[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0819Most_Common_Word/0819Most_Common_Word4.py)

```python
translator = str.maketrans(string.punctuation, ' '*32)
a = paragraph.lower().translate(translator).split()
b = [w for w in a if w not in banned]
return max(b, key = b.count)
```

