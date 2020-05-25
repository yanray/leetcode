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
            if i % 3 == 0 and i % 5 == 0:
                output_str.append("FizzBuzz")
            elif i % 3 == 0:
                output_str.append("Fizz")
            elif i % 5 == 0:
                output_str.append("Buzz")
            else:
                output_str.append(str(i))
                
        return output_str


if __name__ == '__main__':
    a = Solution()

    n = 15
    print(a.fizzBuzz(n))


