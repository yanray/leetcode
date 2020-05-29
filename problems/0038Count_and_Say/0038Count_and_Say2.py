"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return ''.join(self.nextSequence(n, ['1', 'E']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        # print(prevSeq)
        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        # print(prevSeq[0])
        # print(prevSeq[1:])
        for digit in prevSeq[1:]:
            # print(digit)
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1

        # add a delimiter for the next sequence
        nextSeq.append('E')

        # print(nextSeq)
        # print()

        return self.nextSequence(n-1, nextSeq)

if __name__ == '__main__':
    a = Solution()


    n = 4
    print(a.countAndSay(n))

