## Top K Frequent Words

### Problem Link

https://leetcode.com/problems/subarray-sum-equals-k/

### Problem Description 

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

```
Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

```

```
Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

```

**Note:**

* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Input words contain only lowercase letters.

**Follow up:**

* Try to solve it in O(n log k) time and O(n) extra space.

### Code (python)

[Approach 1] (55% - 76%)

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        words_w_times = collections.Counter(words)
        words_in_order = sorted(words_w_times.items(), key = lambda x:(-x[1], x[0]))
        
        return [words_in_order[i][0] for i in range(k)]
```

[Approach 2] (55% - 91%)
```python
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

[Approach 3] (55%)
```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        d=collections.Counter(words)
        ans=[]
        d=d.most_common()
        for each in d :
            if k :
                ans.append(each[0])
                k-=1
            else :
                break
        return ans
```

[Approach 4x] (55%)
```python
from heapq import nsmallest
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return nsmallest(k, freq.keys(), key=lambda x: (-freq[x], x))
```


