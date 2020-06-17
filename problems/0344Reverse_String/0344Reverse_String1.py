"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]


if __name__ == '__main__':
    a = Solution()

    s = ["h","e","l","l","o"]
    print("input: ", s)
    a.reverseString(s)
    print("reversed s: ", s)




