"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
        
        num_al = []
        for ch in s:
            if ch.isdigit():
                num_al.append(ch)
            elif ch.islower():
                num_al.append(ch)
            elif ch.isupper():
                num_al.append(ch.lower())
                
        return num_al == num_al[::-1]


if __name__ == '__main__':
    a = Solution()

    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))

