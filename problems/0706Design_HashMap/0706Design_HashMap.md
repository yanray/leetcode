## Subdomain Visit Count

### Problem Link

https://leetcode.com/problems/subdomain-visit-count/

**Python Counter()**

https://blog.csdn.net/qwe1257/article/details/83272340

### Problem Description 

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.


```
Example 1:

Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

```


```
Example 2:

Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

```


### How to solve 

**Approach 1:** 

Use dictionary, split visit times and domain, extract all subdomain

**Approach 2:** 



### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count1.py)

```python
sub_domain = {}
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)
    sub_d = domain.split('.')
    
    sub_d_length = len(sub_d)
    for j in range(sub_d_length - 1, -1, -1):
        temp = sub_d[sub_d_length - 1]
        for k in range(0, sub_d_length - 1 - j):
            temp = sub_d[sub_d_length - 2 - k] + '.' + temp
            
        if temp in sub_domain:
            sub_domain[temp] += int(times_count)
        else:
            sub_domain[temp] = int(times_count)
        
return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]
        
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count2.py)

```python
sub_domain = {}
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)

    temp = ""
    for subs_d in domain.split('.')[::-1]:
        temp = subs_d + temp
        if temp in sub_domain:
            sub_domain[temp] += int(times_count)
        else:
            sub_domain[temp] = int(times_count)
        temp = '.' + temp

        
return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]

```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0811Subdomain_Visit_Count/0811Subdomain_Visit_Count3.py)

```python
sub_domain = {}
for i, cp_d in enumerate(cpdomains): 
    times_count, domain = cp_d.split(' ', 1)

    temp = ""
    for subs_d in domain.split('.')[::-1]:
        temp = subs_d + temp
        if temp in sub_domain:
            sub_domain[temp] += int(times_count)
        else:
            sub_domain[temp] = int(times_count)
        temp = '.' + temp

        
return [ str(str(v) + ' ' + k) for k, v in sub_domain.items() ]

```
