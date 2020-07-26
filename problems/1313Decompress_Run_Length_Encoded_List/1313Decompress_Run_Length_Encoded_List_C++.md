## Intersection of Two Arrays II

### Problem Link

https://leetcode.com/problems/intersection-of-two-arrays-ii/

### Problem Description 

Given two arrays, write a function to compute their intersection.

```
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

```
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

```

**Note:**

* Each element in the result should appear as many times as it shows in both arrays.
* The result can be in any order.

**Follow up:**

* What if the given array is already sorted? How would you optimize your algorithm?
* What if nums1's size is small compared to nums2's size? Which algorithm is better?
* What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


### Code (python)

[Approach 1: Hash Map] (96%)

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        if(nums1.size() > nums2.size()) 
            return intersect(nums2, nums1);
        
        std::map<int, int> hash_map;
        for(auto num : nums1){
            hash_map[num]++;
        }
        
        int k = 0;
        for(auto num : nums2){
            auto it = hash_map.find(num);
            if(it != hash_map.end() && --it->second >= 0)
                nums1[k++] = num;
        }
        
        return vector(nums1.begin(), nums1.begin() + k);
    }
};
```

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        if(nums1.size() > nums2.size()) 
            return intersect(nums2, nums1);
        
        std::map<int, int> hash_map;
        for(auto num : nums1){
            hash_map[num]++;
        }
        
        int k = 0;
        for(auto num : nums2){
            if(hash_map[num] != '\0' && --hash_map[num] >= 0)
                nums1[k++] = num;
        }
        
        return vector(nums1.begin(), nums1.begin() + k);
    }
};
```

```c++
class Solution {
public:
	vector<int> intersect(vector<int>& num1, vector<int>& num2) {
		vector<int> p;
		unordered_map<int,int> obj;
		for(const auto& num: num1){
			obj[num]++;
		}
		 for(const auto& num: num2){
			obj[num]--;
			 if(obj[num]>=0) p.push_back(num);
		}
		return p;
	}
};
```

[Approach 2: Sort] (96%)

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return intersect(nums2, nums1);
        }
        unordered_map<int, int> m;
        for (auto n : nums1) {
            ++m[n];
        }
        int k = 0;
        for (auto n : nums2) {
            auto it = m.find(n);
            if (it != end(m) && --it->second >= 0) {
                nums1[k++] = n;
            }
        }
        return vector(begin(nums1), begin(nums1) + k);
    }
};
```

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        int i = 0, j = 0;
        vector<int> ans;
        while(i < nums1.size() && j < nums2.size()){
            if(nums1[i] < nums2[j]) i++;
            else if(nums1[i] > nums2[j]) j++;
            else{
                ans.push_back(nums1[i]);
                i++;
                j++;
            }
        }
        return ans;
    }
};
```


[Approach 3: Built-in Intersection] (96)

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(begin(nums1), end(nums1));
        sort(begin(nums2), end(nums2));
        nums1.erase(set_intersection(begin(nums1), end(nums1),
            begin(nums2), end(nums2), begin(nums1)), end(nums1));
        return nums1;
    }
```

```c++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> res(min(nums1.size(), nums2.size()));
        auto it = set_intersection(nums1.begin(), nums1.end(),
                                   nums2.begin(), nums2.end(), res.begin());
        res.resize(it - res.begin());
        return res;
    }
};
```