"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)

        return filtered_chars_list == filtered_chars_list[::-1]


if __name__ == '__main__':
    a = Solution()

    s = "A man, a plan, a canal: Panama"
    print(a.isPalindrome(s))

