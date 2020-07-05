## Word Break

### Problem Link

https://leetcode.com/problems/word-break/

### Problem Description 

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

```
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

```
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

```

```
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

```

### Code (python)

[Approach 1] (80%)

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # dp[i] indicates s[0:i] is whether true or false, i = 1->len-1
        # dp = [False for _ in range(len(s)+1)]
        # for i in range(1,len(s)+1):
        #     if s[0:i] in wordDict:
        #         dp[i] = True
        #     else:
        #         for j in range(i-1,-1,-1):
        #             if dp[j] and s[j:i] in wordDict:
        #                 dp[i] = True
        # return dp[len(s)]
        
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC :: https://www.youtube.com/watch?v=YxtQUbKbdUs ##
        
        ## TIME COMPLEXITY : O(N^2) ##
        ## SPACE COMPLEXITY : O(N) ##

        
        dp = [0] * len(s)               # indicates True or False at that break position
        for i in range(len(s)):
            if s[:i + 1] in wordDict:   # current string till index i is directly found in dict, mark it TRUE
                dp[i] = 1
            else:
                for j in range(i):      # check if the current string can be TRUE, from breaking it (from index 0 to i)
                    if dp[j] and s[j + 1:i + 1] in wordDict:
                        dp[i] = 1
                        break
        return dp[-1]
```

```python
class Solution(object):
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
		# List->Set
        dic = set(wordDict)

        dp = [False for _ in range(n + 1)]
        dp[0] = True
        
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] == True and s[i:j] in dic:
                    dp[j] = True
        
        return dp[-1]
```


[Approach 2] (84%)

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        q = collections.deque()
        q.append(0)
        words = set(wordDict)
        visited = set()
        
        while q:
            start = q.popleft()
            if start == len(s):
                return True
            
            if start in visited:
                continue
                
            visited.add(start)
            for i in range(start, len(s)+1):
                word = s[start:i+1]
                if word in words:
                    q.append(i+1)
        return False
```

https://leetcode.com/problems/word-break/discuss/643456/Sheer-memoization-Python-Easy

https://leetcode.com/problems/word-break/discuss/622750/Python-iterative-trie-%2B-dfs-%2B-lru

https://leetcode.com/problems/word-break/discuss/490911/Python-Simple-Trie-solution-with-detailed-explanation-and-sketches