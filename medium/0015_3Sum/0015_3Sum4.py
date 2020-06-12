"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hash maps (dict) to store neg/pos integer counts.
        neg = {}
        pos = {}
        zeros = 0

        # Hash set to store tuples of valid solutions.
        # Automatically handles duplicate solutions if we add
        # sorted tuples to it.
        solutions = set()

        # Initializing our counter. O(n).
        for i in nums:
            if i < 0:
                neg.setdefault(i, 0)
                neg[i] += 1
            elif i > 0:
                pos.setdefault(i, 0)
                pos[i] += 1
            else:
                zeros += 1

        # We iterate through all unique values of nums.
        # Note: 'i' and 'j' are always opposite in parity. i.e. 'i'
        # and 'j' will never both be positive or both be negative.
        for i in {num for num in nums}:
            # Seeking positive numbers to offset negative numbers.
            if i < 0:
                for j in pos:
                    # Seek for third number, k = -(i + j) 
                    k = -i - j
                    if k in pos:
                        # Invalid solution;
                        if k == j and pos[j]-1 < 1:
                            continue
                        # Valid solution;
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    # If third number is '0' and we have zeros to use.
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            # Logic below is nearly identical logic as above. Kept it verbose for readibility.

            # Seeking negative numbers to offset postive numbers.
            elif i > 0:
                for j in neg:
                    k = -i - j
                    if k in neg:
                        if k == j and neg[j]-1 < 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            # If we encounter a zero, check to see we have 3 or more.
            elif zeros >= 3:
                solutions.add((0, 0, 0))

        return [list(s) for s in solutions]

if __name__ == '__main__':

	a = Solution()

	nums = [-1, 0, 1, 2, -1, -4]

	print("Input: ", nums)
	print("Output: ", a.threeSum(nums))


