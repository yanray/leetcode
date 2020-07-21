## Bulls and Cows

### Problem Link

https://leetcode.com/problems/bulls-and-cows/

### Problem Description 

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

```
Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

```

```
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

```

**Note:** You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

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