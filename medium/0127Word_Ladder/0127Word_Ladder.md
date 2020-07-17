## Word Ladder

### Problem Link

https://leetcode.com/problems/word-ladder/

### Problem Description 

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

**Note:**

* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.

```
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


```

```
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


```

### Code (python)

[Approach 1] (85%)  O(M^2×N)

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
        
        q = collections.deque()
        q.append([beginWord, 1])
        visited_dict = {beginWord: True}
        while q:
            curr_word, level = q.popleft()
            
            for i in range(L):
                
                inter_word = curr_word[:i] + "*" + curr_word[i + 1:]
                
                for word in all_combo_dict[inter_word]:
                    
                    if word == endWord:
                        return level + 1
                    if word not in visited_dict:
                        visited_dict[word] = True
                        q.append([word, level + 1])
                        
                all_combo_dict[inter_word] = []
                
        return 0
```

[Approach 2] (85%)  O(M^2×N)

```python
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0
```

[Approach 3: BFS]

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList: return 0
        # build keys
        memory = {}
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                memory.setdefault(key, []).append(word)
        # almost standard bfs
        visited = set()
        visited.add(beginWord)
        frontier = [beginWord]
        level = 1
        while frontier:
            _next = []
            for word in frontier:
                # find neighbors
                neighbors = []
                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    neighbors += memory.get(key, [])
                # explore the neighbors
                for neighbor in neighbors:
                    # match? we are done here
                    if neighbor == endWord: return level+1
                    if neighbor not in visited:
                        _next.append(neighbor)
                        visited.add(neighbor)
            level += 1
            frontier = _next
        return 0
```