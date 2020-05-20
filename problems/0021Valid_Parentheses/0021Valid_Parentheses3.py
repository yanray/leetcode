"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def isValid(self, s):
        while '()'in s or '{}' in s or '[]' in s:
          s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''


if __name__ == '__main__':
    a = Solution()
    input_string = "({[]})"
    print(a.isValid(input_string))
