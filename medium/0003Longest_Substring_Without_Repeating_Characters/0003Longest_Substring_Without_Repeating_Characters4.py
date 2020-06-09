"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        str_dict = {}
        start, max_len = 0, 0
        for i in range(len(s)):
            if s[i] in str_dict:
                start = max(str_dict[s[i]], start)
            max_len = max(max_len, i - start + 1)
            str_dict[s[i]] = i + 1
        return max_len

if __name__ == '__main__':
 
    a = Solution()

    s = "abba"

    print("input: ", s)
    print("output: ", a.lengthOfLongestSubstring(s))


