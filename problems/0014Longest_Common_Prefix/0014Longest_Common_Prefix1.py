"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        else:
            prefix = strs[0]
            for s in strs:
                temp = prefix
                if temp == "":
                    return prefix
                else:
                    prefix = ""
                    for i in range(min(len(temp), len(s))):
                        if temp[i] == s[i]:
                            prefix += s[i]
                        else:
                            break

            return prefix


if __name__ == '__main__':
    a = Solution()

    # strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    strs = []
    print(a.longestCommonPrefix(strs))

