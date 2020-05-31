"""

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
    # Explaination: Ordered Dict will save the characters it encounters in
    # same sequence as the original string. Hence it becomes easy to catch hold of the first
    #unique character. Then according to the counter variable, whenever the first 1 is encountered
    # the corresponding dict.key's index is returned from the original String.
        for i,j in collections.OrderedDict(collections.Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1

if __name__ == '__main__':
    a = Solution()

    s = "leetcode"

    print(a.firstUniqChar(s))


    
