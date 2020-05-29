"""

Version: 1.1 
Author:  Yanrui 
date:    5/28/2020
"""

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
            

if __name__ == '__main__':
    a = Solution()


    n = 10
    print(a.countPrimes(n))

