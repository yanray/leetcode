"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/25/2020
"""

import collections

class Solution:
    def subdomainVisits(self, cpdomains):
        
        sub_domain = collections.Counter()
        for i, cp_d in enumerate(cpdomains): 
            times_count, domain = cp_d.split(' ', 1)
            frags = domain.split('.')

            for i in range(len(frags)):
                sub_domain['.'.join(frags[i:])] += int(times_count)

                
        return [ "{0} {1}".format(v, k) for k, v in sub_domain.items() ]
            


if __name__ == '__main__':
    a = Solution()

    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    # cpdomains = ["9001 discuss.leetcode.com"]

    print(a.subdomainVisits(cpdomains))


