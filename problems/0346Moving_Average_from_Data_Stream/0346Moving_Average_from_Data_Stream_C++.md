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

[Approach 2] (%) 

```c++
#include <iostream>
#include <deque>
#include <numeric>
using namespace std;
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(const int& size) {
        this->dq.clear();
        this->size = size;
    }
    
    double next(const int& val) {
        this->dq.push_front(val);
        if (this->dq.size() < this->size) 
            return double(accumulate(dq.begin(), dq.end(), 0.0)) / double(this->dq.size());
        else
            return double(accumulate(dq.begin(), dq.begin() + this->size, 0.0)) / double(this->size);
    }
private:
    deque<int> dq;
    int size;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */

int main(int argc, char** argv) {
	MovingAverage m(3);
	return 0;
}
```

[Approach 3] (67%) 

```c++
class MovingAverage {
public:
    private:
        vector<int> q;
        int window_size;
        int sum_val;
        int i = 0;
    
    public:
    /** Initialize your data structure here. */
    MovingAverage(int size): window_size(size), sum_val(0){
    }
    
    double next(int val) {
        sum_val += val;
         
        if(q.size() < window_size){
            q.push_back(val);
            return double(sum_val) / q.size();
        }
        else{
            i =  i % window_size; 
            sum_val -= q[i];
            q[i++] = val;
            return double(sum_val) / window_size;
        }
    }
};
```