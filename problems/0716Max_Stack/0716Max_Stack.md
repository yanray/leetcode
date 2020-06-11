## Max Stack

### Problem Link

https://leetcode.com/problems/max-stack/

### Problem Description 

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

```
Example 1: 

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

```

**Note:**

1. -1e7 <= x <= 1e7
2. Number of operations won't exceed 10000.
3. The last four operations won't be called when stack is empty.

### How to solve 

**Approach 1:** 


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0122Best_Time_to_Buy_and_Sell_Stock_II/0122Best_Time_to_Buy_and_Sell_Stock_II1.py)

```python
# if prices == sorted(prices, reverse = True):
#     return 0

valley = peak = 0
len_price = len(prices)
max_profit = 0
i = 0
while i < len_price - 1:
    while i < len_price - 1 and prices[i] >= prices[i + 1]:
        i += 1
    valley = prices[i]

    while i < len_price - 1 and prices[i] <= prices[i + 1]:
        i += 1
    peak = prices[i]
    max_profit += peak - valley
    
return max_profit
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0122Best_Time_to_Buy_and_Sell_Stock_II/0122Best_Time_to_Buy_and_Sell_Stock_II2.py)

```python
max_profit = 0 
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        max_profit += prices[i] - prices[i - 1]
        
return max_profit 
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0122Best_Time_to_Buy_and_Sell_Stock_II/0122Best_Time_to_Buy_and_Sell_Stock_II3.py)

```python
return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
```
