## Squares of a Sorted Array

### Problem Link

https://leetcode.com/problems/squares-of-a-sorted-array/

### Problem Description 

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

```
Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

```

```
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

**Note:**

* 1 <= A.length <= 10000
* -10000 <= A[i] <= 10000
* A is sorted in non-decreasing order.



### Code (python)

[Approach 1] (5% - 15%)

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        if not A:
            return []
        if len(A) == 1:
            return [A[0] ** 2]
        
        squares_A = []
        left, right = 0, len(A) - 1
        s_lf, s_rt = A[left] ** 2, A[right] ** 2
        while left < right:
            if s_lf >= s_rt:
                squares_A.append(s_lf)
                left += 1
                s_lf = A[left] ** 2
            else:
                squares_A.append(s_rt)
                right -= 1
                s_rt = A[right] ** 2
        squares_A.append(s_lf)
                
        return squares_A[::-1]
```

(%) O(N)

```python
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans
```

(45% - 55%)

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        if not A:
            return []
        if len(A) == 1:
            return [A[0] ** 2]
        
        squares_A = deque()
        left, right = 0, len(A) - 1
        s_lf, s_rt = A[left] ** 2, A[right] ** 2
        while left < right:
            if s_lf >= s_rt:
                squares_A.appendleft(s_lf)
                left += 1
                s_lf = A[left] ** 2
            else:
                squares_A.appendleft(s_rt)
                right -= 1
                s_rt = A[right] ** 2
        squares_A.appendleft(s_lf)
                
        return squares_A
```

(sort)
[Approach 2] 

(75%)
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
    
        squares_A = []
        for i in range(len(A)):
            squares_A.append(A[i] ** 2)
            
        return sorted(squares_A)
```

(30% - 99%) O(NlogN)

```python
class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)
```