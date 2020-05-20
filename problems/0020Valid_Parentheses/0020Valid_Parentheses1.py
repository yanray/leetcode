"""
Valid Parentheses

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def isValid(self, s):
      if len(s):
          parenthese_left = ['(', '{', '[']
          parenthese_right = [')', '}', ']']
          num_record = []
          for i in range(len(s)):
              if s[i] in parenthese_left:
                  # print('position 1')
                  # print(parenthese_left.index(s[i]))
                  num_record.append(parenthese_left.index(s[i]))
              else:
                  # print('position 2')
                  if not len(num_record):
                      return False
                  elif(parenthese_right.index(s[i]) == num_record[len(num_record) - 1]):
                      # print('ready to pop')
                      # print('num_record:', num_record)
                      num_record.pop()
                      # print('after pop')
                      # print('num_record:', num_record)
                  else:
                      return False
          if not len(num_record):
              return True
          else:
              return False
      else:
          return True


if __name__ == '__main__':
    a = Solution()
    input_string = "({[]})"
    print(a.isValid(input_string))
