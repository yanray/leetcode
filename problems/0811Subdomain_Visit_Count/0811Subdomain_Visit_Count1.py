"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/25/2020
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        
        sub_domain = {}
        for i, cp_d in enumerate(cpdomains): 
            times_count, domain = cp_d.split(' ', 1)
            sub_d = domain.split('.')
            
            sub_d_length = len(sub_d)
            for j in range(sub_d_length - 1, -1, -1):
                temp = sub_d[sub_d_length - 1]
                for k in range(0, sub_d_length - 1 - j):
                    temp = sub_d[sub_d_length - 2 - k] + '.' + temp
                    
                if temp in sub_domain:
                    sub_domain[temp] += int(times_count)
                else:
                    sub_domain[temp] = int(times_count)
                
        return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]
            


if __name__ == '__main__':
    a = Solution()

    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    # cpdomains = ["9001 discuss.leetcode.com"]

    print(a.subdomainVisits(cpdomains))


