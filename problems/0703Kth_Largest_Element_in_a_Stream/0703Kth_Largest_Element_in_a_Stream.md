## Kth Largest Element in a Stream

### Problem Link

https://leetcode.com/problems/kth-largest-element-in-a-stream/

### Problem Description 

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.


```
Example 1:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

```

**Note:**

You may assume that nums' length ≥ k-1 and k ≥ 1.

### Code (python)

https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/639723/AC-simply-readable-Python-heap-bisect

https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/427268/Python-3-line-O(TlogN)-%2B-4-line-O(Tlogk)

[Approach 1] (99%)

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.arr = nums
        
        heapify( self.arr) 
        
        # Keep popping smaller elemnts till size = k
        while len( self.arr ) > self.k:
            heappop( self.arr )

    def add(self, val: int) -> int:
        
        heap_top = 0
        
        # Always keep heap size = k
        # Top element = kth largest element
        if len( self.arr ) < self.k:
            heappush( self.arr, val)
        else:
            heappushpop( self.arr, val)
        
        return self.arr[heap_top]
```

[Approach 2] (95%)

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k: heapq.heappush(self.heap, val)            
        else: heapq.heappushpop(self.heap, val)
        return self.heap[0]
```

[Approach 3] (80%)

```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):        
        self.k = k
        self.heap = heapq.nlargest(self.k, nums)[::-1]
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k: heapq.heappush(self.heap, val)            
        else: heapq.heappushpop(self.heap, val)
        return self.heap[0]
```

[Approach 4] (67%)

```python
class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element
```