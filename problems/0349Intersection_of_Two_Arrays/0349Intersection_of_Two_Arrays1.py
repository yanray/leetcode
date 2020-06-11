"""

Version: 1.1 
Author:  Yanrui 
date:    06/11/2020
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':

    a = Solution()

    nums1 = [1,2,2,1]
    nums2 = [2,2]

    print("nums1:", nums1)
    print("nums2:", nums2)

    print(a.intersection(nums1, nums2))
