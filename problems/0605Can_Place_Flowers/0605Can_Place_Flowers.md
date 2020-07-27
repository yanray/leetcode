## Can Place Flowers

### Problem Link

https://leetcode.com/problems/can-place-flowers/

### Problem Description 


Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

```
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

```

```
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

```

**Note:**

1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. n is a non-negative integer which won't exceed the input array size.


### Code (python)

[Approach 1] (5%)

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        left, right = -2, 0
        count = 0
        
        while right < len(flowerbed):
            if flowerbed[right] == 1:
                num_of_zero = (right - left) - 3
                if num_of_zero > 0:
                    count += (num_of_zero + 1) // 2
                left = right
                
            right += 1
                
        if flowerbed[-1] != 1:
            num_of_zero = (right - left) - 2
            if num_of_zero > 0:
                count += (num_of_zero + 1) // 2
        
        return count >= n
```