"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/22/2020
"""


class Solution:
    def reorderLogFiles(self, logs):
      new_log = []
      letters_dic = {}        # build a dictionary to connect letters size and corresponding number in logs file
      digit_log = []          # order digit log seperately
      letters_log = []            # order digit log seperately

      for i in range(0, len(logs)):
          for j in range(0, len(logs[i])):
              if logs[i][j] == ' ':
                  if logs[i][j + 1].isdigit():
                      digit_log.append(logs[i])
                  else:
                      letters_log.append(logs[i])
                  break

      letters_log.sort()
      for i in range(0, len(letters_log)):
          for j in range(0, len(letters_log[i])):
              if letters_log[i][j] == ' ':
                  letters_dic[i] = letters_log[i][j + 1 : len(letters_log[i])]
                  break

      letters_dic = sorted(letters_dic.items(), key = lambda x: x[1]) # (reverse = True)

      for i in range(0, len(letters_dic)):
          num = letters_dic[i][0]
          new_log.append(letters_log[num])

      return new_log + digit_log


if __name__ == '__main__':
  a = Solution()

  # logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
  logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

  print("Output: ", a.reorderLogFiles(logs))


