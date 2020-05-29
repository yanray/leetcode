## Count and Say

### Problem Link

https://leetcode.com/problems/count-and-say/

### Problem Description 

The count-and-say sequence is the sequence of integers with the first five terms as following:
 
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

```
Example 1: 

Input: 1
Output: "1"
Explanation: This is the base case.

```

```
Example 2: 

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".

```


### How to solve 

**Approach 1:** 

埃氏筛选法: 对于筛选整数n以内的素数，算法是这么描述的：先把素数2的倍数全部删除，剩下的数第一个为3，再把素数3的倍数全部删除，剩下的第一个数为5，再把素数5的倍数全部删除······直到把n以内最后一个素数的倍数删除完毕，得到n以内的所有素数。


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0204Count_Primes/0204Count_Primes1.py)

```python
if n <= 2:
    return 0

num_list = [1] * n
num_list[0] = 0
num_list[1] = 0
num_list[2] = 1

for i in range(1, int(n ** 0.5) + 1):
    if num_list[i] == 0:
        continue
    else:
        num_list[i] = 1
        for j in range(i * i, n, i):
            num_list[j] = 0

return sum(num_list)
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0204Count_Primes/0204Count_Primes2.py)

```python
class Solution:
    
    def sieve_algorithm(self, n: int)-> bool:
        
        if n <= 2:
			# Corner case handle
            return 0
        
        
        is_prime = [ True for _ in range(n) ]
        
        # Base case initialization
        is_prime[0] = False
        is_prime[1] = False
        
        upper_bound = int(n ** 0.5)
        for i in range( 2, upper_bound+1 ):
            
            if not is_prime[i]:
                # only run on prime number
                continue
            
            
            for j in range( i*i, n, i):
                # mark all multiples of i as "not prime"
                is_prime[j] = False
                
        return sum(is_prime)
    
    
    
    def countPrimes(self, n: int) -> int:
        
        return self.sieve_algorithm(n)
            
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0204Count_Primes/0204Count_Primes3.py)

```python
if n < 3: return 0
dp = [0, 0] + [1] * (n - 2)
for i in range(2, int(n ** 0.5) + 1):
    if dp[i]: dp[i ** 2:n:i] = [0] * len(dp[i ** 2:n:i])
return sum(dp)
```

[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0204Count_Primes/0204Count_Primes4.py)

```python
if n < 3: return 0
dp = [0, 0] + [1] * (n - 2)
for i in range(2, int(n ** 0.5) + 1):
    if dp[i]: dp[i ** 2:n:i] = [0] * len(dp[i ** 2:n:i])
return sum(dp)
```