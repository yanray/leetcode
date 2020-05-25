"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def fizzBuzz(self, n):
        
        output_str = []
        for i in range(1, n + 1):

            divisable_by_3 = (i % 3 == 0)
            divisable_by_5 = (i % 5 == 0)

            temp = ""
            if divisable_by_3:
                temp += "Fizz"
            if divisable_by_5:
                temp += "Buzz"
            if not temp:
                temp = str(i)

            output_str.append(temp)
                
        return output_str


if __name__ == '__main__':
    a = Solution()

    n = 15
    print(a.fizzBuzz(n))


