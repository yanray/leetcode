"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""
from typing import List
import collections

class Solution:
    def compress(self, chars: List[str]) -> int:

        # char_dict = collections.Counter(chars)

        # return len(char_dict) if len(char_dict) > 1 else 1

        if len(chars) == 1:
            return 1

        count_ch = 1
        pointer = 0
        for i in range(len(chars) - 1):
            if (i + 2) == len(chars) and chars[i + 1] == chars[pointer]:
                chars[pointer + 1] = str(count_ch + 1)
                pointer += 2
            elif (i + 2) == len(chars) and chars[i + 1] != chars[pointer]:
                chars[pointer + 1] = str(count_ch)
                chars[pointer + 2] = chars[i + 1]
                pointer += 3
            elif chars[i] == chars[pointer] and chars[i + 1] == chars[pointer]:
                count_ch += 1
            elif chars[i] == chars[pointer] and chars[i + 1] != chars[pointer]:
                if count_ch == 1:
                    chars[pointer + 1] = chars[i + 1]
                    pointer += 1
                else:
                    chars[pointer + 1] = str(count_ch)
                    chars[pointer + 2] = chars[i + 1]
                    pointer += 2
                    count_ch = 1


        return chars[:pointer]


if __name__ == '__main__':
    a = Solution()

    chars = ["a","a","b","b","c","c", "c", "d", "d"]
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(a.compress(chars))

