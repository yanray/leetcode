## Group Anagrams

### Problem Link

https://leetcode.com/problems/group-anagrams/

### Problem Description 

Given an array of strings, group anagrams together.

```
Example 1:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

```

**Note:**

* All inputs will be in lowercase.
* The order of your output does not matter.

### Code (python)

[Approach 1] (10%)

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        result = []
        seen = []
        
        for i in range(len(strs)):
            temp = collections.Counter(strs[i])
            if temp in seen:
                index = seen.index(temp)
                result[index].append(strs[i])
            else:
                result.append([strs[i]])
                seen.append(temp)
                
        return result
```

[Approach 2: Categorize by Sorted String] (80%) O(NKlogK)

```python
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```

```python
import collections
class Solution:
    
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

		hashmap = collections.defaultdict(list)
		# sort the word and make it as a key in hashmap and append the unsorted word.
		for word in strs:
			sorted_word = ''.join(sorted(word))
			hashmap[sorted_word].append(word)        

	return [v for k,v in hashmap.items()]
```

```python
class Solution(object):
    def groupAnagrams(self, strs):
        anagramDic = {}
        for word in strs:
            currentAnagram = "".join(sorted(word))
            if currentAnagram not in anagramDic:
                anagramDic[currentAnagram] = [word]
            else:
                anagramDic[currentAnagram].append(word)
        return list(anagramDic.values())
```

[Approach 3: Categorize by Count] (40%) O(NK)

```python
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```

https://leetcode.com/problems/group-anagrams/discuss/721497/C%2B%2B-and-Python-solutions