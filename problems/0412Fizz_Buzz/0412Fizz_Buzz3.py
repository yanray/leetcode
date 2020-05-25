"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def fizzBuzz(self, n):
        
        output_str = []

        mapping_dict = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):
            temp = ""

            for key in mapping_dict.keys():
                if i % key == 0:
                    temp += mapping_dict[key]

            if not temp:
                temp = str(i)

            output_str.append(temp)
                
        return output_str


if __name__ == '__main__':
    a = Solution()

    n = 15
    print(a.fizzBuzz(n))


