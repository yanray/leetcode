"""

Version: 1.1 
Author:  Yanrui 
date:    5/24/2020
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[:] = sorted(nums1[:m] + nums2)        


if __name__ == '__main__':
    a = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3

    print("nums1 = ",nums1)
    print("nums2 = ", nums2)
    a.merge(nums1, m, nums2, n)
    print("after merge, nums1 = ",nums1)



