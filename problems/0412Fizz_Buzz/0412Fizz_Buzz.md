## Fizz Buzz

### Problem Link
https://leetcode.com/problems/fizz-buzz/

### Problem Description 

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

```
Example1:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

```


### How to solve 

**Approach 1:** 

Naive

**Approach 2:** 

String Concatenation

**Approach 3:** 

Hash it!

1. Put all the mappings in a hash table. The hash table fizzBuzzHash would look something like { 3: 'Fizz', 5: 'Buzz' }

2. Iterate on the numbers from 1 ... N1...N.

3. For every number, iterate over the fizzBuzzHash keys and check for divisibility.

4. If the number is divisible by the key, concatenate the corresponding hash value to the answer string for current number. We do this for every entry in the hash table.

5. Add the answer string to the answer list.

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0412Fizz_Buzz/0412Fizz_Buzz1.py)

```python
output_str = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        output_str.append("FizzBuzz")
    elif i % 3 == 0:
        output_str.append("Fizz")
    elif i % 5 == 0:
        output_str.append("Buzz")
    else:
        output_str.append(str(i))
        
return output_str
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0412Fizz_Buzz/0412Fizz_Buzz2.py)

```python
output_str = []
for i in range(1, n + 1):

    divisable_by_3 = (i % 3 == 0)
    divisable_by_5 = (i % 5 == 0)

    temp = ""
    if divisable_by_3:
        temp += "Fizz"
    if divisable_by_5:
        temp += "Buzz"
    if not temp:
        temp = str(i)

    output_str.append(temp)
        
return output_str
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0412Fizz_Buzz/0412Fizz_Buzz3.py)

```python
return words == sorted(words, key = lambda w: [order.index(x) for x in w])
```