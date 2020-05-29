"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def countPrimes(self, n: int) -> int:

        num_list = [1] * n
        num_list[0] = 0
        num_list[1] = 0
        num_list[2] = 1

        for i in range(1, int(n ** 0.5) + 1):
            if num_list[i] == 0:
                continue
            else:
                num_list[i] = 1
                for j in range(i * i, n, i):
                    num_list[j] = 0

        print(num_list)
        return sum(num_list)

if __name__ == '__main__':
    a = Solution()


    n = 10
    print(a.countPrimes(n))

