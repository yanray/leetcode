## Majority Element

### Problem Link

https://leetcode.com/problems/majority-element/

### Problem Description 


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

```
Example 1:

Input: [3,2,3]
Output: 3

```

```
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

```

### How to solve 

**Approach 1:**

Use collections.Counter

**Approach 2:**

Use dictionary to count numbers
Hashing

**Approach 3 - 4:**

Look the code !



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0169Majority_Element/0169Majority_Element1.py)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_dict = collections.Counter(nums)
        for k, v in hash_dict.items():
            if v >= len(nums) // 2 + 1:
                return k
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0169Majority_Element/0169Majority_Element2.py)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1
                
            if hash_dict[nums[i]] >= len(nums) // 2 + 1:
                return nums[i]
```

```python
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        new_dict = {}
        for key in nums:
            if key not in dict:
                new_dict[key] = 1
            else:
                new_dict[key] += 1
        #check for the maximum value and return the key associated with it
        return max(new_dict, key = dict.get)
```

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=len(nums)//2
        o=defaultdict(int)
        for i in nums:
            o[i]+=1
        for key,value in o.items():
            if value>a:
                return key
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0169Majority_Element/0169Majority_Element3.py)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## RC ##
        ## LOGIC ##
        #   Boyer-Moore Voting Algorithm
        ## NOTE : WORKS ONLY IF ELEMENT OCCURENCE IS MORE THAN HALF OF ARRAY SIZE ##
        # Ex : [7, 7, 5, 7, 5, 1 , 5, 7 , 5, 5, 7, 7 , 7, 7, 7, 7]
        ## STACK TRACE ##
        ## count , candidate
        # 1 7
        # 2 7
        # 1 7
        # 2 7
        # 1 7
        # 0 7
        # 1 5
        # 0 5
        # 1 5
        # 2 5
        # 1 5
        # 0 5
        # 1 7
        # 2 7
        # 3 7
        # 4 7
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            #print(count, candidate)
        return candidate
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0169Majority_Element/0169Majority_Element4.py)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
```