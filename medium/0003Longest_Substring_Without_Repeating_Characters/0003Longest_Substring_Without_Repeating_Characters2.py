"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        str_list = []
        max_length = 0
        
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
                
            str_list.append(x)    
            max_length = max(max_length, len(str_list))
            
        return max_length

if __name__ == '__main__':
 
    a = Solution()

    s = "abba"

    print("input: ", s)
    print("output: ", a.lengthOfLongestSubstring(s))


