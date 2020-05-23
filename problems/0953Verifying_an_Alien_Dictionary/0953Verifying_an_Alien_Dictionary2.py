"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def isAlienSorted(self, words, order):
        hashmap = {c:i for i, c in enumerate(order)}
        return words == sorted(words, key = lambda w: [hashmap[x] for x in w])


if __name__ == '__main__':
    a = Solution()

    words = ["hello","leetcode"]

    order = "hlabcdefgijkmnopqrstuvwxyz"

    print(a.isAlienSorted(words, order))


