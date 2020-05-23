"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def isAlienSorted(self, words, order):
        right_order = 'abcdefghijklmnopqrstuvwxyz'
        
        trans = str.maketrans(order, right_order)
        new_words = [w.translate(trans) for w in words]
        
        for i in range(len(new_words) - 1): 
            if new_words[i] > new_words[i + 1]:
                return False
        
        return True


if __name__ == '__main__':
    a = Solution()

    words = ["hello","leetcode"]

    order = "hlabcdefgijkmnopqrstuvwxyz"

    print(a.isAlienSorted(words, order))


