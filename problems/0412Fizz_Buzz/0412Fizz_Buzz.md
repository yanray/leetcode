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

把words里的字母按照order里面的顺序替换成正常顺序 所对应的new words, 然后比较大小判断顺序

**Approach 2:** 

根据order创建一个hashmap，根据hashmap对应的顺序对words进行重新排序，看words是否等于排序后的words

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary1.py)

```python
right_order = 'abcdefghijklmnopqrstuvwxyz'

trans = str.maketrans(order, right_order)
new_words = [w.translate(trans) for w in words]

for i in range(len(new_words) - 1): 
    if new_words[i] > new_words[i + 1]:
        return False

return True    
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary2.py)

```python
hashmap = {c:i for i, c in enumerate(order)}
return words == sorted(words, key = lambda w: [hashmap[x] for x in w])
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0953Verifying_an_Alien_Dictionary/0953Verifying_an_Alien_Dictionary3.py)

```python
return words == sorted(words, key = lambda w: [order.index(x) for x in w])
```