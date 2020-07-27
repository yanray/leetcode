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

[Approach 2: Single Scan, check neighbor]  (92%)

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        L    = len(flowerbed)
        last = False    # planted last turn
        for i,x in enumerate(flowerbed):
            can = False # can plant now
            if not x and not last:
                can = True
                if i>0 and flowerbed[i-1]:
                    can = False
                if i<(L-1) and flowerbed[i+1]:
                    can = False
                if can:
                    n -= 1
                    if n<1:
                        break
            last = can
        return n<1
```

[Approach 3: Three Solutions in Python 3 (beats ~100%)]

```python
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        L, i, c, f = len(f)-2, -2, 0, f + [0]
        while i < L:
        	i += 2
        	if f[i] == 1: continue
        	if f[i+1] == 0: c += 1
        	else: i += 1
        return n <= c
		
		
		
		
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
    	L, f, i, c = len(f), [0] + f + [0], 1, 0
    	while i <= L:
    		if f[i-1:i+2] == [0,0,0]: c, i = c + 1, i + 1
    		i += 1
    	return n <= c
		
		
		
		
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
    	L, f, s, c = len(f), f + [0,1], 0, 1
    	for i in range(L+2):
    		if f[i] == 1: s, c = s + max(0,c-1)//2, 0
    		else: c += 1
    	return n <= s
```

[Approach 4: Count Zeros] (97%)

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        zero = 1  # initial has no left limit
        for slot in flowerbed:
            if slot == 0:
                zero += 1
            else:
                n -= (zero - 1) // 2 if zero else 0
                zero = 0
        n -= zero / 2  # last has no right limit
        return n <= 0
```