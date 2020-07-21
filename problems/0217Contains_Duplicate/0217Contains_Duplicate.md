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

[Approach 1] (90%) 

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bull = 0
        cows = 0
        index_list = []
        hash_dict = collections.defaultdict(int)
        
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bull += 1
            else:
                index_list.append(i)
                hash_dict[secret[i]] += 1
            
        for i in range(len(index_list)):
            val = hash_dict.get(guess[index_list[i]], 0)
            if val > 0:
                hash_dict[guess[index_list[i]]] -= 1
                cows += 1
                
        return str(bull) + "A" + str(cows) + "B"
```


[Approach 2] (78%) 

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(s == g for s,g in zip(secret, guess))
        b = collections.Counter(secret) & collections.Counter(guess)
        return f'{a}A{sum(b.values()) - a}B'

```

(97%)

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
		# The main idea is to understand that cow cases contain the bull cases
		
		# This loop will take care of "bull" cases
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        
		# This loop will take care of "cow" cases
        cows=0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        
        return f"{bull}A{cows-bull}B"
```


[Approach 3] (97%)

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        unmatched_secret = [0] * 10
        unmatched_guess = [0] * 10
        bulls = 0
        for x, y in zip(secret, guess):
            x, y = int(x), int(y)
            if x == y:
                bulls += 1
            else:
                unmatched_secret[x] += 1
                unmatched_guess[y] += 1
        cows = sum(min(unmatched_secret[i], unmatched_guess[i]) for i in range(10))
        return f'{bulls}A{cows}B'
```