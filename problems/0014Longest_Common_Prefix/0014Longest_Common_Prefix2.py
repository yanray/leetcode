"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

from typing import List

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False  # this field is to identify a word



class TrieTree:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        parent = self.root

        # in case the input is "", we need to mark the node as a word as below for loop does not execute
        if len(word) == 0:
            parent.isWord = True

        for i, ch in enumerate(word):
            if ch not in parent.children:
                parent.children[ch] = TrieNode(ch)
            parent = parent.children[ch]
            if i == len(word)-1:
                parent.isWord = True

    def longestPrefix(self):
        parent = self.root
        prefix = ""
        
        # if for any node, if isWord = True, it represents a the first word in the list, 
        # longest common prefix (lcp) cannot be longer than the shortest word.
        # if any node has more than one child, root to till that node should be lcp.
        while not parent.isWord and len(parent.children) == 1:
        # take the first child, we do not need other children as we break out of while loop if that node has more children
            ch = list(parent.children)[0]
            prefix += ch
            parent = parent.children[ch]

        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        root = TrieTree()
        curr = root

        for word in strs:
            root.insert(word)

        prefix = root.longestPrefix()

        return prefix


if __name__ == '__main__':
    a = Solution()

    strs = ["flower","flow","flight"]
    # strs = ["dog","racecar","car"]
    # strs = []
    print(a.longestCommonPrefix(strs))

