## Partition Labels

### Problem Link

https://leetcode.com/problems/partition-labels/

### Problem Description 

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

```
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

```

**Note:**

1. S will have length in range [1, 500].
2. S will consist of lowercase English letters ('a' to 'z') only.

### Code (python)

[Approach 1] (60%) 

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        if not S:
            return []
        
        hash_dict = {}
        for i in range(len(S)):
            hash_dict[S[i]] = i
            
        
        def helper(S, index):
            
            length = hash_dict[S[index]]

            while index < length:
                length = max(length, hash_dict[S[index]])
                index += 1
        
            return [S[index + 1:], index + 1]
        
        result = []
        temp = S
        index = 0
        pre_index = 0
        
        while temp != "":
            temp, index = helper(S, index)
            result.append(index - pre_index)
            pre_index = index
        
        return result
```

[Approach 2: Greedy] (60%) 

```python
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

[Approach 3] (97%)

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []
        partition_chars = []
        right_indexes = {}
        i = 0 #string char count
        j = 1 #partition char count
        for x in S:
            if x not in partition_chars:
                partition_chars.append(x)
                right_indexes[x] = S.rindex(x)
            if i == right_indexes[x]:
                partition_chars.remove(x)
                if len(partition_chars) == 0:
                    result.append(j)
                    j = 0                 
            j += 1
            i += 1
                    
        return result
```