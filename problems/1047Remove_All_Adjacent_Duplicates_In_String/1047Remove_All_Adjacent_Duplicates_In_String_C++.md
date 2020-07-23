## Remove All Adjacent Duplicates In String

### Problem Link

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

### Problem Description 

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

```
Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

**Note:**

1. 1 <= S.length <= 20000
2. S consists only of English lowercase letters.

### Code (python)

[Approach 1] (94%) 

```c++
class Solution {
public:
    string removeDuplicates(string S) {
        
        string s1 = "";
        
        for(char ch : S){
            if(!s1.empty() && s1.back() == ch) s1.pop_back();
            else s1.push_back(ch);
        }
        
        return s1;
    }
};
```

```c++
class Solution {
public:
    string removeDuplicates(string S) {
        string sRes = "";
        for (const auto& c : S) {
            // cout << "c:" << c << endl;
            if (!sRes.empty() && sRes.back() == c)
                sRes.pop_back();
            else
                sRes.push_back(c);
        }
        return sRes;
    }
};
```

[Approach 2: Stack] 

```c++
class Solution {
public:
    string removeDuplicates(string S) {

        stack<int> st;
        
        for(char ch : S){
            if(!st.empty() && ch == st.top()) st.pop();
            else st.push(ch);
        }
        
        string s1 = "";
        while(!st.empty()){
            s1 += st.top();
            st.pop();
        }
        
        reverse(s1.begin(), s1.end());
        return s1;
    }
};
```