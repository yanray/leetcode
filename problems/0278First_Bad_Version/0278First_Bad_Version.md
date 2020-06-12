## Product of Array Except Self

### Problem Link

https://leetcode.com/problems/product-of-array-except-self/

### Problem Description 

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

```
Example 1: 

Input:  [1,2,3,4]
Output: [24,12,8,6]

```

**Constraint:** It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

**Note:** Please solve it without division and in O(n).

**Follow up:**
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


### How to solve 

**Approach 1 - 2:** 

Left and Right product lists

**Approach 3:** 

O(1) space

**Approach 4:** 

Left and Right product lists: One Pass, O(1) space

https://leetcode.com/problems/product-of-array-except-self/discuss/681707/AC-optimized-Python-O(1)-Space-one-pass


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0238Product_of_Array_Except_Self/0238Product_of_Array_Except_Self1.py)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_len = len(nums)
        from_left = [1]
        from_right = [1]
        product_nums = []
        
        for i in range(nums_len - 1):
            from_left.append(from_left[-1] * nums[i])
        
        for i in range(nums_len - 1, 0, -1):
            from_right.append(from_right[-1] * nums[i])
            
        for i in range(nums_len):
            product_nums.append(from_left[i] * from_right[nums_len - 1 - i])
            
        return product_nums
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0238Product_of_Array_Except_Self/0238Product_of_Array_Except_Self2.py)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/medium/0238Product_of_Array_Except_Self/0238Product_of_Array_Except_Self3.py)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/medium/0238Product_of_Array_Except_Self/0238Product_of_Array_Except_Self4.py)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:     
        n = len(nums)
        l, r, s = 1, 1, [1]*n
        for i in range(n):
            s[i] *= l
            l *= nums[i]
            s[~i] *= r
            r *= nums[~i]            
        return s
```

[Approach 5](https://github.com/yanray/leetcode/blob/master/medium/0238Product_of_Array_Except_Self/0238Product_of_Array_Except_Self5.py)

```python

```