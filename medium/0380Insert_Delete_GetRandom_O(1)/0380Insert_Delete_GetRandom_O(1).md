## Time Based Key-Value Store

### Problem Link

https://leetcode.com/problems/time-based-key-value-store/

### Problem Description 

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

* Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)

* Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
* If there are multiple such values, it returns the one with the largest timestamp_prev.
* If there are no values, it returns the empty string ("").

```
Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   


```

```
Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]

```

**Note:**

1. All key/value strings are lowercase.
2. All key/value strings have length in the range [1, 100]
3. The timestamps for all TimeMap.set operations are strictly increasing.
4. 1 <= timestamp <= 10^7
5. TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.

### Code (python)

[Approach 1] (50%)

```python
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_dict:
            temp = self.hash_dict[key]
            index = bisect.bisect_right(temp[1], timestamp)
            temp[0].insert(index, value)
            temp[1].insert(index, timestamp)
        else:
            self.hash_dict[key] = [[value], [timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_dict:
            temp = self.hash_dict[key]
            if timestamp < temp[1][0]:
                return ""
            else:
                index = bisect.bisect_right(temp[1], timestamp)
                return temp[0][index - 1]
        else:
            return ""
```

[Approach 2] (76%) (O(1) and log(N))

```python
class TimeMap(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""
```

```python
class TimeMap(object):

    def __init__(self):
        self.map = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        values = self.map[key]
        if not values: return ''
        left, right = 0, len(values) - 1
        while left < right:
            mid = (left + right + 1) / 2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                left = mid
        return values[left][1] if values[left][0] <= timestamp else ''
```

```python
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.d:
            return ""
        
        arr = self.d[key]; i = len(arr)-1
        while i >= 0 and arr[i][1] > timestamp:
            i -= 1
        return arr[i][0] if i >= 0 else ""

```

https://leetcode.com/problems/time-based-key-value-store/discuss/537385/Python-solution-Using-Hash-%2B-LinkedList.-Another-way-to-solve-the-problem.

[Approach 3] (60%+)

```python
class TimeMap:

    def __init__(self):
        # dictionary: key -> max-heap ordered by timestamp
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            heap = self.dict[key]
        else:
            heap = []
            self.dict[key] = heap
        
        # negate timestamp to emulate max-heap
        heappush(heap, (-timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            heap = self.dict[key]
            # search through heap until we find the first element with a valid timestamp
            for val in heap:
                if -val[0] <= timestamp:
                    return val[1]
        return ""
```