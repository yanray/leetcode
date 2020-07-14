## Sum of Two Integers

### Problem Link

https://leetcode.com/problems/binary-tree-paths/

### Problem Description 

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

```
Example 1:

Input: a = 1, b = 2
Output: 3

```

```
Example 2:

Input: a = -2, b = 3
Output: 1

```

### Code (python)

[Approach 1] (100%) 

```c++
class Solution {
public:
    int getSum(int a, int b) {
        while(b){
            int carry = (unsigned int)(a & b) << 1;  // unsigned int to handle negitive numbers
            a ^= b;
            b = carry;
        }
        return a;
    }
};
```

[Approach 2] (100%) 

```c++
class Solution {
public:
    int getSum(int a, int b) {
            return b? getSum(a^b, (unsigned int)(a&b)<<1):a;
        }
    }
};
```

[Approach 3] (100%) 

```c++
class Solution {
public:
    int getSum(int a, int b) {
        if (b==0) return a;
        
        int sum = a^b; // finding the sum
        int carry = (unsigned int)(a & b)<<1; // finding the carry
        return getSum(sum, carry);
    }
};
```