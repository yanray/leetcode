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

遍历挨着查

**Approach 2:** 

Sliding Window: 

* Within the function, we scan the sequence with two contextual variables: prevDigit and digitCnt which refers to respectively the digit that we are expecting in the sub-sequence and the number of occurrence of the digit in the sub-sequence.
* At the end of each sub-sequence, we append the summary to the result and then we reset the above two contextual variables for the next sub-sequence.
* Note that, we use an artificial delimiter in the sequence to facilitate the iteration.

**Approach 2:**

Regular Expression: https://blog.csdn.net/weixin_38256474/article/details/83278333

```python
regex = "((.)*)"
```

* "(.)": again, this is a group that contains a single character that could be of anything.

* "": this part refers to the second group (i.e. (.)) that we define.

* "((.)*)": the outer bracket defines the scope of the first group, which contains the repetitive appearance of the second group above.

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0038Count_and_Say/0038Count_and_Say1.py)

```python
cs_sequence = ["0", "1"]

for i in range(1, n):
    prev_cs_str = cs_sequence[i]
    
    cs_str = ""
    num_count = 0
    for j, ch in enumerate(prev_cs_str):
        if (j + 1) == len(prev_cs_str) or prev_cs_str[j + 1] != ch:
            cs_str += str(num_count + 1) + ch
            num_count = 0
        elif prev_cs_str[j + 1] == ch:
            num_count += 1

    cs_sequence.append(cs_str)
    
return cs_sequence[n]
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0038Count_and_Say/0038Count_and_Say2.py)

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return ''.join(self.nextSequence(n, ['1', 'E']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1

        # add a delimiter for the next sequence
        nextSeq.append('E')

        return self.nextSequence(n-1, nextSeq)
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0038Count_and_Say/0038Count_and_Say3.py)

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        currSeq = '1'
        pattern = r'((.)\2*)'

        for i in range(n-1):
            nextSeq = []
            for g1, g2 in re.findall(pattern, currSeq):
                print(currSeq)
                print(re.findall(pattern, currSeq))
                print('g1', g1)
                print('g2', g2)
                print()
                # append the pair of <count, digit>
                nextSeq.append(str(len(g1)))
                nextSeq.append(g2)
            # prepare for the next iteration
            currSeq = ''.join(nextSeq)

        return currSeq
```