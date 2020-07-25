## Find Pivot Index

### Problem Link

https://leetcode.com/problems/find-pivot-index/

### Problem Description 

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

```
Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

```

```
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

```


### Code (python)

[Approach 1] 

(32%) 

```c++
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        long long total = accumulate(nums.begin(), nums.end(), 0);
        
        int index = 0;
        int left_sum = 0;
        while(index < nums.size()){
            total -= nums[index];
            
            if(left_sum == total) return index;
            
            left_sum += nums[index];
            index += 1;
        }
        
        return -1;
    }
};
```

(51%)

```c++
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int total = 0;
        for(int i = 0; i < nums.size(); i++){
            total += nums[i];
        }
        
        int index = 0;
        int left_sum = 0;
        while(index < nums.size()){
            total -= nums[index];
            
            if(left_sum == total) return index;
            
            left_sum += nums[index];
            index += 1;
        }
        
        return -1;
    }
};
```

[Approach 2] (77%)

```c++
class Solution {
public:
    int pivotIndex(vector<int>& num) {
        int n = num.size();
        int sumTotal = 0;
        int sumLeft = 0;
        if (n == 0)
        {
            return -1;
        }
		/* Sum all the elements in the array */
        for (int i = 0; i < n; i++)
        {
            sumTotal += num[i];
        }
        
        /* The logic is that once we get the sum on the right == sum on the left we will have 
            total sum - num[i] = 2*left sum*/
        for (int i = 0; i < n; i++)
        {
            if (sumTotal - num[i]  == 2*sumLeft)
            {
                return i;
            }
            sumLeft += num[i];
        }
        return -1; 
    }
};
```

[Approach 3]

```c++
class Solution {
public:
    int pivotIndex(vector<int>& num) {
        if(num.size()<2)
            return num.size()-1;
        int i,s=0,c=0;
        for(i=0;i<num.size();i++)
        {
            s+=num[i];
        }
        for(i=0;i<num.size();i++)
        {
            if(c==(s-num[i]-c))
                return i;
            c+=num[i];
        }
        return -1;
    }
};
```