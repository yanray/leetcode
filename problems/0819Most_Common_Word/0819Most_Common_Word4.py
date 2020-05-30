"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

from typing import List
import string
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        translator = str.maketrans(string.punctuation, ' '*32)
        a = paragraph.lower().translate(translator).split()
        b = [w for w in a if w not in banned]
        return max(b, key = b.count)

if __name__ == '__main__':
    a = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = "hit"

    print(a.mostCommonWord(paragraph, banned))


    
