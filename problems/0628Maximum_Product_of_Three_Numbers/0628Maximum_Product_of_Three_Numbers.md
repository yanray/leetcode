## Maximum Product of Three Numbers

### Problem Link

https://leetcode.com/problems/maximum-product-of-three-numbers/

### Problem Description 

Given an integer array, find three numbers whose product is maximum and output the maximum product.

```
Example 1:

Input: [1,2,3]
Output: 6

```

```
Example 2:

Input: [1,2,3,4]
Output: 24

```

**Note:**

* The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
* Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

### Code (python)

[Approach 1] (95%) (O(nlogn))

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
```

https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/412859/Python3

https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/353426/Three-Solutions-in-Python-3-(beats-~100)-(-O(n)-)

[Approach 2: Heap] (%) (O(nlogn))

```python
class Solution:
    def maximumProduct(self, n: List[int]) -> int:
    	a = heapq.nsmallest(2,n)
    	b = heapq.nlargest(3,n)
    	return max(b[0]*b[1]*b[2],b[0]*a[0]*a[1])
```

[Approach 3] () (O(N))

```java
public class Solution {
    public int maximumProduct(int[] nums) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE, max3 = Integer.MIN_VALUE;
        for (int n: nums) {
            if (n <= min1) {
                min2 = min1;
                min1 = n;
            } else if (n <= min2) {     // n lies between min1 and min2
                min2 = n;
            }
            if (n >= max1) {            // n is greater than max1, max2 and max3
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (n >= max2) {     // n lies betweeen max1 and max2
                max3 = max2;
                max2 = n;
            } else if (n >= max3) {     // n lies betwen max2 and max3
                max3 = n;
            }
        }
        return Math.max(min1 * min2 * max1, max1 * max2 * max3);
    }
}
```