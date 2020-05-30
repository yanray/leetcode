"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""

from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # convert to lower case and split string into words by spaces and punctuation
        a = re.split(r'\W+', paragraph.lower())
        
        # make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned]
        
        # return value that counted max times in the new list
        return max(b, key = b.count)


if __name__ == '__main__':
    a = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = "hit"

    print(a.mostCommonWord(paragraph, banned))


    
