## Kth Largest Element in an Array

### Problem Link

https://leetcode.com/problems/kth-largest-element-in-an-array/

### Problem Description 

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

```
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

```

```
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

```

**Note:**

You may assume k is always valid, 1 ≤ k ≤ array's length.

### Code (python)

[Approach 1] (87%) 

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort(reverse = True)
        return nums[k - 1]
```

[Approach 2] (80%) O(Nlogk)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
```

Finally the overall algorithm is quite straightforward :

* Choose a random pivot.

* Use a partition algorithm to place the pivot into its perfect position pos in the sorted array, move smaller elements to the left of pivot, and larger or equal ones - to the right.

* Compare pos and N - k to choose the side of array to proceed recursively.

[Approach 3: Quickselect] (%) O(N)

```python
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)
```

```python
from random import uniform
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # transform into the k smallest
        k = len(nums)-k
        # solve kth smallest in O(n)
        def quick_select(nums, k):
            # get a random pivot
            pivot = int(uniform(0, len(nums)))
            # smaller than pivot -> left, bigger -> right
            left, right = [], []
            for i, e in enumerate(nums):
                if e <= nums[pivot] and i != pivot: left.append(e)
                if e > nums[pivot]: right.append(e)
            # match with k, we are done
            if k == len(left): return nums[pivot]
            # keep exploring
            if k < len(left):
                return quick_select(left, k)
            else:
                return quick_select(right, k-len(left)-1)
        return quick_select(nums, k)
```

```python
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = self.getPivot(nums)
        
        if p+1 == k: return nums[p]
        elif p+1 > k: return self.findKthLargest(nums[:p], k)
        else: return self.findKthLargest(nums[p+1:],k-1-p)
        
    def getPivot(self, nums):
        lo,hi = 0, len(nums)-1
        if lo>=hi: return lo
        self.swap(nums, random.randrange(lo,hi,1), hi)
        i = lo
        for j in range(lo, hi):
            if nums[j]>nums[hi]:
                self.swap(nums, i , j)
                i+=1
        self.swap(nums,i,hi)
        return i
        
    def swap(self, nums, i ,j):
        nums[i], nums[j] = nums[j], nums[i]
        return nums
```
