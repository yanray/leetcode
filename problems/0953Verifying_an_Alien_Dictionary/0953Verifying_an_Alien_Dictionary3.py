"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def isAlienSorted(self, words, order):
    	return words == sorted(words, key = lambda w: [order.index(x) for x in w])


if __name__ == '__main__':
    a = Solution()

    words = ["hello","leetcode"]

    order = "hlabcdefgijkmnopqrstuvwxyz"

    print(a.isAlienSorted(words, order))


