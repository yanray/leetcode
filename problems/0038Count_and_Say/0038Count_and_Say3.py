"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""
import re

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        currSeq = '1'
        pattern = r'((.)\2*)'

        for i in range(n-1):
            nextSeq = []
            for g1, g2 in re.findall(pattern, currSeq):
                print(currSeq)
                print(re.findall(pattern, currSeq))
                print('g1', g1)
                print('g2', g2)
                print()
                # append the pair of <count, digit>
                nextSeq.append(str(len(g1)))
                nextSeq.append(g2)
            # prepare for the next iteration
            currSeq = ''.join(nextSeq)

        return currSeq

if __name__ == '__main__':
    a = Solution()


    n = 5
    print(a.countAndSay(n))

