"""
Reverse Linked List

Version: 1.1 
Author:  Yanrui 
date:    5/30/2020
"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        s = []
        while head:
            s.append(str(head.val))
            head = head.next

        return s == s[::-1]


if __name__ == '__main__':
    a = Solution()


    


