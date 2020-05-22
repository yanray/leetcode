"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/22/2020
"""


class Solution:
    def reorderLogFiles(self, logs):
        digit_log = []
        letters_log = []
        
        for ll in logs:
            if ll[-1].isdigit():
                digit_log.append(ll)
            else:
                letters_log.append(ll)
        
        letters_log.sort(key = lambda x: (x[x.index(' ') + 1: ], x[: x.index(' ') ]))
        
        return letters_log + digit_log


if __name__ == '__main__':
  a = Solution()

  # logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
  logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

  print("Output: ", a.reorderLogFiles(logs))


