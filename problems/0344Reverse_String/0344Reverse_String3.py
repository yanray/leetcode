"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List

class Solution:
    def reverseString(self, s):
        s.reverse()


if __name__ == '__main__':
    a = Solution()

    s = ["h","e","l","l","o"]
    print("input: ", s)
    a.reverseString(s)
    print("reversed s: ", s)




