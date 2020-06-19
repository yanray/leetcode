## Kth Largest Element in a Stream

### Problem Link

https://leetcode.com/problems/kth-largest-element-in-a-stream/

### Problem Description 

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

```
Example 1:

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

```

**Note:**
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

### Code (python)

[Approach 1] (87%-99%)

```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        index1 = -1
        index2 = -1
        shortest = len(words)
        for i in range(len(words)):
            if word1 == words[i]:
                index1 = i
            elif word2 == words[i]:
                index2 = i
                
            if index1 != -1 and index2 != -1:
                shortest = min(shortest, abs(index1 - index2))
                # if shortest == 1:
                    # return shortest
                
        return shortest
```

[Approach 2] ()

```python
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        min_dist = len(words)
        curr_word, idx = None, 0
        for i, w in enumerate(words):
            if w not in (word1, word2): continue
            if curr_word and w != curr_word:
                min_dist = min(min_dist, i - idx)
            curr_word, idx = w, i
        return min_dist
```
