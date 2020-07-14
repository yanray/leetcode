## Moving Average from Data Stream

### Problem Link

https://leetcode.com/problems/moving-average-from-data-stream/

### Problem Description 

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

```
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

```

### Code (python)

[Approach 1] (20%) 

```c++
class MovingAverage {
public:
    private:
        int window_size;
        std::queue<int> q;
        int sum_val;
    
    public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        window_size = size;
        sum_val = 0;
    }
    
    double next(int val) {
        if (q.size() == window_size){
            sum_val -= q.front();
            q.pop();
        }
        sum_val += val;
        q.push(val);
        
        return double(sum_val) / q.size();
    }
};
```