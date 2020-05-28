"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    a = Solution()

    s = "A man, a plan, a canal: Panama"

    print(a.isPalindrome(s))

