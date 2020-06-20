## K Closest Points to Origin

### Problem Link

https://leetcode.com/problems/k-closest-points-to-origin/

### Problem Description 

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


```
Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

```

```
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

```

Note:

* 1 <= K <= points.length <= 10000
* -10000 < points[i][0] < 10000
* -10000 < points[i][1] < 10000

### Code (python)

[Approach 1] (50 - 60%)

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for i in range(len(points)):
            dis = sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            heapq.heappush(heap, [dis, points[i]])
            
        K_closest = []
        for i in range(K):
            K_closest.append(heapq.heappop(heap)[1])
            
        return K_closest
```

(60 - 65%)

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        len_points = len(points)
        
        for i in range(len_points - K):
            dis = sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            heapq.heappush(heap, [dis, points[i]])
            
        K_closest = []
        for i in range(K):
            dis = sqrt(points[len_points - K + i][0] * points[len_points - K + i][0] + points[len_points - K + i][1] * points[len_points - K + i][1])
            K_closest.append(heapq.heappushpop(heap, [dis, points[len_points - K + i]])[1])
            
        return K_closest
```

[Approach 2] ()

```python

```