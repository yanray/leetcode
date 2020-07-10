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

