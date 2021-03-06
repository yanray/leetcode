## Letter Combinations of a Phone Number

### Problem Link

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

### Problem Description 

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

hash_dict = {"2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"], 
            "4" : ["g", "h", "i"], 
            "5" : ["j", "k", "l"], 
            "6" : ["m", "n", "o"], 
            "7" : ["p", "q", "r", "s"], 
            "8" : ["t", "u", "v"], 
            "9" : ["w", "x", "y", "z"]}

```
Example 1:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

### Code (python)

[Approach 1] (94%)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        hash_dict = {"2" : ["a", "b", "c"],
                     "3" : ["d", "e", "f"], 
                     "4" : ["g", "h", "i"], 
                     "5" : ["j", "k", "l"], 
                     "6" : ["m", "n", "o"], 
                     "7" : ["p", "q", "r", "s"], 
                     "8" : ["t", "u", "v"], 
                     "9" : ["w", "x", "y", "z"]}
        
        result = hash_dict[digits[-1]]
        for i in range(len(digits) - 2, -1, -1):
            temp = []
            mapping = hash_dict[digits[i]]
            for j in range(len(mapping)):
                for k in range(len(result)):
                    temp.append(mapping[j] + result[k])
                    
            result = temp
        
        
        return result
```

[Approach 2: Backtracking] (80%) 

```python
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
```

https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/671244/Python-The-itertools-way-of-doing-it
