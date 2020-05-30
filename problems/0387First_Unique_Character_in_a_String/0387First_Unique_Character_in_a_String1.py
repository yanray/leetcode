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
        
        old_punc = string.punctuation
        new_punc = ' ' * len(string.punctuation)
        words = paragraph.translate(str.maketrans(old_punc, new_punc)).lower().split()

        words_dict = collections.Counter(words)

        for i in range(len(words_dict)):
            temp = words_dict.most_common(1)[0][0]
            if temp in banned:
                del words_dict[temp]
            else:
                return temp


if __name__ == '__main__':
    a = Solution()

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = "hit"

    print(a.mostCommonWord(paragraph, banned))


    
