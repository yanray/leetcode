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

[Approach 1] (55%) 

```c++
class Solution {
public:
    string getHint(string secret, string guess) {
        
        unordered_map<char, int> hash_map;
        int bulls = 0, cows = 0;
        
        for(int i = 0; i < secret.size(); i++){
            if(guess[i] == secret[i]) bulls++;
            else hash_map[secret[i]]++;
        }
        
        for(int i = 0; i < guess.size(); i++){
            if(hash_map[guess[i]] > 0 && guess[i] != secret[i]){
                cows++;
                hash_map[guess[i]]--;
            }
        }
        
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};

```

[Approach 2] (55%)

```c++
class Solution {
public:
    string getHint(string secret, string guess) {
        int bullCnt{}, cowCnt{};
        for (int i{}; i < secret.size(); ++i)
        {
		// Only if the characters are the same and in the same position
		// can we state we've found a bull.
            if (secret[i] == guess[i])
            {
                bullCnt++;
                secret[i] = '*';
                guess[i] = '*';
            }
        }

        for (int i{}; i < guess.size(); ++i)
        {
			// Only asses positions that are not already starred.
			// Save the location of positions that we find in the string secret.
            if (int location = secret.find(guess[i]); guess[i] != '*' && location != string::npos)
            {
			// We found a letter from guess in secret. This means we have a cow.
			// Mark the given character in both strings as used.
                cowCnt++;
                secret[location] = '*';
                guess[i] = '*';
            }
        }
        
        string res = to_string(bullCnt) + 'A' + to_string(cowCnt) + 'B';
        return res;
        
    }
};
```