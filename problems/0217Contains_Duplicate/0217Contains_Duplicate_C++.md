## Contains Duplicate

### Problem Link

https://leetcode.com/problems/contains-duplicate/

### Problem Description 

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

```
Example 1:

Input: [1,2,3,1]
Output: true

```

```
Example 2:

Input: [1,2,3,4]
Output: false

```

```
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

```

### Code (python)

[Approach 1] (96%) 

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        if(nums.size() == 0) return false;
        
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] == nums[i + 1]) return true;
        }
        
        return false;
    }
};
```

[Approach 2] (34%) 

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        unordered_set<int> set;
        for(int num : nums) set.insert(num);
        
        if(set.size() == nums.size()) return false;
        else return true;
    }
};
```

[Approach 3] (31%)

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
          unordered_map<int, int>umap;
          for (int i = 0; i < nums.size(); i++)
          {
              umap[nums[i]] = i;
          }

          for (int i = 0; i < nums.size(); i++)
          {
              if (umap.find(nums[i]) != umap.end())
                  umap.erase(nums[i]);
              else
                  return true;
          }
          return false;
    }
};

```

[Approach 4: Three very simple yet efficient solutions in C++]

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set;
        for(int i = 0; i < nums.size(); ++i) if(!nums_set.insert(nums[i]).second) return true;
        return false;
    }
};
```

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > unordered_set<int>(nums.begin(), nums.end()).size();
    }
};
```

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return distance(unique(nums.begin(), nums.end()), nums.end());
    }
};
```