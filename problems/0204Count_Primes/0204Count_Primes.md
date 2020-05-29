## Count Primes

### Problem Link
https://leetcode.com/problems/count-primes/

Link: https://blog.csdn.net/Snow_Me/article/details/52588819

### Problem Description 

Count the number of prime numbers less than a non-negative number, n.
 
**Follow up:**
Could you solve it using only O(1) extra space?

```
Example: 

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

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

