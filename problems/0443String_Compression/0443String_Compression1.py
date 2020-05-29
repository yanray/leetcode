"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""
from typing import List
import collections

class Solution:
    def compress(self, chars: List[str]) -> int:

        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write


if __name__ == '__main__':
    a = Solution()

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(a.compress(chars))

