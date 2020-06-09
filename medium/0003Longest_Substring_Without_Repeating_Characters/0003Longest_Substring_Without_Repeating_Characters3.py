"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r,m,d=0,0,0,set()
        while r < len(s):
            if not s[r] in d:
                d.add(s[r])
                m = max(len(d),m)
                r += 1
            else:
                d.remove(s[l])
                l += 1
        return m

if __name__ == '__main__':
 
    a = Solution()

    s = "abba"

    print("input: ", s)
    print("output: ", a.lengthOfLongestSubstring(s))


