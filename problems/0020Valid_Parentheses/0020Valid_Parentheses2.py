"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def isValid(self, s):
      left = ['(', '{', '[']
      right = [')', '}', ']']
      Stack = []
      for letter in s:
        if letter in left:
          Stack.append(letter)
        elif letter in right:
          if len(Stack) <= 0:
            return False
          if left.index(Stack.pop()) != right.index(letter):
              return False
      return len(Stack) == 0



if __name__ == '__main__':
    a = Solution()
    input_string = "({[]})"
    print(a.isValid(input_string))
