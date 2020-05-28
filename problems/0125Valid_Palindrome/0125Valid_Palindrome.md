## Longest Common Prefix

### Problem Link
https://leetcode.com/problems/longest-common-prefix/

### Problem Description 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


```
Example 1: 

Input: ["flower","flow","flight"]
Output: "fl"

```

```
Example 2: 

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

### How to solve 

**Approach 1:** 

Horizontal scanning, util the end of the List[string] or prefix == ""

**Approach n:** 

https://leetcode.com/problems/longest-common-prefix/solution/

* **Veritical scanning:** 从第一个字符开始依次比较

* **Divide and Conquer:** 分成左右子集, 找到common prefix in left and right, 再common

* **Binary Search:** 寻找strs里最短的字符串, 先比较left是不是都是prefix, 如果是, 往右判断, 如果不是, 往左判断

```java
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0)
        return "";
    int minLen = Integer.MAX_VALUE;
    for (String str : strs)
        minLen = Math.min(minLen, str.length());
    int low = 1;
    int high = minLen;
    while (low <= high) {
        int middle = (low + high) / 2;
        if (isCommonPrefix(strs, middle))
            low = middle + 1;
        else
            high = middle - 1;
    }
    return strs[0].substring(0, (low + high) / 2);
}

private boolean isCommonPrefix(String[] strs, int len){
    String str1 = strs[0].substring(0,len);
    for (int i = 1; i < strs.length; i++)
        if (!strs[i].startsWith(str1))
            return false;
    return true;
}
```

查找最短字符串
```python
strings = ["some", "example", "words", "that", "i", "am", "fond", "of"]
print min(strings, key=len) # prints "i"

```

**Approach 2:** 

* **Use Trie:** 

Reference: https://leetcode.com/problems/longest-common-prefix/discuss/642674/Python-solution-with-Trie-(with-explanation)

https://leetcode.com/articles/implement-trie-prefix-tree/


**Approach 3:** 

Use min and max to compare find common prefix

**Approach 4:** 

Use zip fucntion, zip function 

```python
print(list(zip(*strs)))
```

**Approach 5:** 

return os.path.commonprefix(strs)

**Approach 6:** 

vertical scanning


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix1.py)

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        else:
            prefix = strs[0]
            for s in strs:
                temp = prefix
                if temp == "":
                    return prefix
                else:
                    prefix = ""
                    for i in range(min(len(temp), len(s))):
                        if temp[i] == s[i]:
                            prefix += s[i]
                        else:
                            break

            return prefix
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix2.py)

```python
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False  # this field is to identify a word



class TrieTree:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        parent = self.root

        # in case the input is "", we need to mark the node as a word as below for loop does not execute
        if len(word) == 0:
            parent.isWord = True

        for i, ch in enumerate(word):
            if ch not in parent.children:
                parent.children[ch] = TrieNode(ch)
            parent = parent.children[ch]
            if i == len(word)-1:
                parent.isWord = True

    def longestPrefix(self):
        parent = self.root
        prefix = ""
        
        # if for any node, if isWord = True, it represents a the first word in the list, 
        # longest common prefix (lcp) cannot be longer than the shortest word.
        # if any node has more than one child, root to till that node should be lcp.
        while not parent.isWord and len(parent.children) == 1:
        # take the first child, we do not need other children as we break out of while loop if that node has more children
            ch = list(parent.children)[0]
            prefix += ch
            parent = parent.children[ch]

        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        root = TrieTree()
        curr = root

        for word in strs:
            root.insert(word)

        prefix = root.longestPrefix()

        return prefix
```



[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix3.py)

```python
if not strs: 
    return ""
s1 = min(strs)
s2 = max(strs)
for i,x in enumerate(s1):
    if x != s2[i]:
        return s2[:i]
return s1
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix4.py)

```python
if not strs: 
    return ""
s1 = min(strs)
s2 = max(strs)
for i,x in enumerate(s1):
    if x != s2[i]:
        return s2[:i]
return s1
```


[Approach 5](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix5.py)

```python
return os.path.commonprefix(strs)
```



[Approach 6](https://github.com/yanray/leetcode/blob/master/problems/0014Longest_Common_Prefix/0014Longest_Common_Prefix6.py)

```python
res, i, j = '', 0, 0
try:
    while True:
        if i == len(strs) - 1:
            res += strs[0][j]
            i = 0
            j += 1
        if strs[i][j] == strs[i+1][j]:
            i += 1
        else:
            return res
except:
    return res
```