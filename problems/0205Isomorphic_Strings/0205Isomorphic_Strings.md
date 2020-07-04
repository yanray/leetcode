## Isomorphic Strings

### Problem Link

https://leetcode.com/problems/isomorphic-strings/

### Problem Description 

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

```
Example 1:

Input: s = "egg", t = "add"
Output: true

```

```
Example 2:

Input: s = "foo", t = "bar"
Output: false

```

```
Example 3:

Input: s = "paper", t = "title"
Output: true

```

**Note:**

You may assume both s and t have the same length.



### Code (python)

[Approach 1] (10% - 25%)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        d = {}
        for ix, ch in enumerate(s):
            if ch not in d:
                if t[ix] in d.values():
                    return False
                d[ch] = t[ix]
            else:
                if d[ch] != t[ix]:
                    return False
        return True
```

[Approach 2] (fast)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word_dic = {}

        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                if(s[i] in word_dic):
                    if(word_dic[s[i]]!=t[i]):
                        return False
                else:
                    if(t[i] in list(word_dic.values())):
                        return False
                    word_dic[s[i]] = t[i]

        return True
```


[Approach 2] (fast)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word_dic = {}

        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                if(s[i] in word_dic):
                    if(word_dic[s[i]]!=t[i]):
                        return False
                else:
                    if(t[i] in list(word_dic.values())):
                        return False
                    word_dic[s[i]] = t[i]

        return True
```

[Approach 3] (fast)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## RC ##
        ## APPROACH : HASHMAP ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##   ( we can have utmost 0-9a-zA-Z and special symbols 256 length )

        s_map = {}
        t_map = {}
        for i in range(len(s)):
            # map the characters of both strings, 
            # if you find a char already mapped and the current values are not similar to what we have mapped before return False
            if (s[i] in s_map and s_map[s[i]] != t[i]) or (t[i] in t_map and t_map[t[i]] != s[i]):
                    return False
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        return True
```

[Approach 4] (fast)

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 记录一个字符上次出现的位置，如果两个字符串中的字符上次出现的位置一样，那么就属于同构。
        preIndexOfS, preIndexOfT = [0]*256, [0]*256
        for i in range(len(s)):
            sch,tch=s[i],t[i]
            if preIndexOfS[ord(sch)]!=preIndexOfT[ord(tch)]:
                return False
            preIndexOfS[ord(sch)],preIndexOfT[ord(tch)] = i+1, i+1
        return True
```

[Approach 5] (95%)

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """   
        s_index = [ s.find(i) for i in s ]
        t_index = [ t.find(i) for i in t ]
        return s_index == t_index
```