"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        
        cs_sequence = ["0", "1"]
        
        for i in range(1, n):
            prev_cs_str = cs_sequence[i]
            
            cs_str = ""
            num_count = 0
            for j, ch in enumerate(prev_cs_str):
                if (j + 1) == len(prev_cs_str) or prev_cs_str[j + 1] != ch:
                    cs_str += str(num_count + 1) + ch
                    num_count = 0
                elif prev_cs_str[j + 1] == ch:
                    num_count += 1

            cs_sequence.append(cs_str)
            
        return cs_sequence[n]

if __name__ == '__main__':
    a = Solution()


    n = 5
    print(a.countAndSay(n))

