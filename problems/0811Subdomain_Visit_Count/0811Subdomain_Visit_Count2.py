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

            temp = ""
            for subs_d in domain.split('.')[::-1]:
                temp = subs_d + temp
                if temp in sub_domain:
                    sub_domain[temp] += int(times_count)
                else:
                    sub_domain[temp] = int(times_count)
                temp = '.' + temp

                
        return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]
            


if __name__ == '__main__':
    a = Solution()

    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    # cpdomains = ["9001 discuss.leetcode.com"]

    print(a.subdomainVisits(cpdomains))


