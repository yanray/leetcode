## Strobogrammatic Number

### Problem Link

https://leetcode.com/problems/strobogrammatic-number/

### Problem Description 

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

```
Example 1:

Input: num = "69"
Output: true

```

```
Example 2:

Input: num = "88"
Output: true

```

```
Example 3:

Input: num = "962"
Output: false

```

```
Example 4:

Input: num = "1"
Output: true

```


### Code (python)

[Approach 1: map] (100%)

```c++
class Solution {
public:
    bool isStrobogrammatic(string num) {
        
        std :: map<char, char> hash_map = {{'0', '0'}, 
                                           {'1', '1'},
                                           {'6', '9'},
                                           {'8', '8'},
                                           {'9', '6'}};
        
        int n = num.size() - 1;
        for(int i = 0; i < num.size() / 2 + 1; i++){
            if(hash_map[num[i]] != num[n - i]) return false;
        }
        
        return true;
        
    }
};
```

[Approach 2: reverse] (100%)

```c++
class Solution {
public:
    bool isStrobogrammatic(std::string n) 
    {
        const auto nOriginal = n;

        std::reverse(n.begin(), n.end());

        // do not touch 0, 1, 8
        // touch 6 and 9

        for(auto &el: n)
        {
            if(el == '9')
            {
                el = '6';
            }
            else if(el == '6')
            {
                el = '9';
            }
            else if(el != '0' && el != '8' && el != '1')
            {
                return false;
            }
        }

        return n == nOriginal;
        
    }
};
```