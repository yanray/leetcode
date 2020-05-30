"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

from typing import List
import string
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans


if __name__ == '__main__':
    a = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = "hit"

    print(a.mostCommonWord(paragraph, banned))


    
