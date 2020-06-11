"""

Version: 1.1 
Author:  Yanrui 
date:    06/11/2020
"""

from typing import List

class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


if __name__ == '__main__':

    a = Solution()

    nums1 = [1,2,2,1]
    nums2 = [2,2]

    print("nums1:", nums1)
    print("nums2:", nums2)

    print(a.intersection(nums1, nums2))
