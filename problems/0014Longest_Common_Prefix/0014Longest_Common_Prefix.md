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

