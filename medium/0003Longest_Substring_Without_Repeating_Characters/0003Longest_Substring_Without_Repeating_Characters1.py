"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        sub_str_dict = {}
        sub_len = [1]
        sub_str_dict[s[0]] = 0

        for i in range(1, len(s)):
            if s[i] in sub_str_dict:
                sub_len.append(min(i - sub_str_dict[s[i]], sub_len[i - 1] + 1))
                sub_str_dict[s[i]] = i
            else:
                sub_str_dict[s[i]] = i
                sub_len.append(sub_len[i - 1] + 1)

        return max(sub_len)

if __name__ == '__main__':
 
    a = Solution()

    s = "abba"

    print("input: ", s)
    print("output: ", a.lengthOfLongestSubstring(s))


