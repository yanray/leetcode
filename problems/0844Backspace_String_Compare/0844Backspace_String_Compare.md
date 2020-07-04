## Backspace String Compare

### Problem Link

https://leetcode.com/problems/backspace-string-compare/

### Problem Description 

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

```
Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

```

```
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

```

```
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

```

```
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

```

**Note:**

* 1 <= S.length <= 200
* 1 <= T.length <= 200
* S and T only contain lowercase letters and '#' characters.

**Follow up:**

* Can you solve it in O(N) time and O(1) space?


### Code (python)

[Approach 1: Build String] (85%)

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def build_str(s):
            new_s = []
            for ch in s:
                if ch != "#":
                    new_s.append(ch)
                elif new_s:
                    new_s.pop()
                    
            return new_s
        
        return build_str(S) == build_str(T)
```

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(S: str) -> str:
            str_s = ''
            for i in range(len(S)):
                if S[i] != '#':
                    str_s += S[i]
                else:
                    str_s = str_s[:-1]
            return str_s
        return get_str(S) == get_str(T)
```


[Approach 2: Two Pointers] (85%) (only for python)

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```

O(N)

```python
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S), len(T) # two indexes, start outside of string to make loop simpler
        
        while i >= 0 and j >= 0:
            back = 1 # backspace counter, move back at least one character
            while back > 0:
                i -= 1
                back += 1 if i >= 0 and S[i] == '#' else -1 # if hashtag found increase backspace counter, otherwise decrease it

            back = 1
            while back > 0:
                j -= 1
                back += 1 if j >= 0 and T[j] == '#' else -1
            
            if i >= 0 and j >= 0 and S[i] != T[j]: # done with backspaces, compare current character
                return False
        
        return i < 0 and j < 0 # return True if both indexes passed both strings fully
```


```python
class Solution:
	def backspaceCompare(self, S, T):
		i = len(S) - 1			# Traverse from the end of the strings
		j = len(T) - 1

		skipS = 0              # The number of backspaces required till we arrive at a valid character
		skipT = 0

		while i >= 0 or j >= 0:
			while i >= 0:					# Ensure that we are comparing a valid character in S
				if S[i] == "#" :
					skipS += 1				# If not a valid character, keep times we must backspace.
					i = i - 1

				elif skipS > 0:
					skipS -= 1				# Backspace the number of times calculated in the previous step
					i = i - 1

				else:
					break

			while j >= 0:					# Ensure that we are comparing a valid character in T
					if T[j] == "#":
						skipS += 1			# If not a valid character, keep times we must backspace.
						j = j - 1

					elif skipT > 0:
						skipT -= 1			# Backspace the number of times calculated in the previous step
						j = j - 1

					else:
						break

			print("Comparing", S[i], T[j])		# Print out the characters for better understanding.

			if i>= 0 and j >= 0 and S[i] != T[j]:    # Compare both valid characters. If not the same, return False.
				return False

			if (i>=0) != (j>=0):		# Also ensure that both the character indices are valid. If it is not valid,
				return False			#  it means that we are comparing a "#" with a valid character.

			i = i - 1
			j = j - 1

		return True					# This means both the strings are equivalent.
```