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

(70%)

```python
class Solution:
    def get_tuple(self, x, y):
        val = -(x*x + y*y)
        point = (x,y)
        return (val, point)
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []        
        heap = []
        for i in range(K):
            heapq.heappush(heap, self.get_tuple(points[i][0], points[i][1]))
        
        for i in range(K, len(points)):
            tup = self.get_tuple(points[i][0], points[i][1])
            heapq.heappushpop(heap, tup)
        
        for item in heap:
            res.append(item[1])
        
        return res
```

Sort

[Approach 2] (88% - 95%, NlogN)

```python
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
```

heap

[Approach 3] (67%)

```python
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, lambda x: x[0] ** 2 + x[1] ** 2)
```


(No heap, No sort)

[Approach 4] (5%)

```python
class Solution(object):
    def sortArray(self, left, right):
        l_idx, r_idx = 0, 0
        to_return_points = []
        while l_idx < len(left) and r_idx < len(right):
            l_dist = left[l_idx][0]**2 + left[l_idx][1]**2
            r_dist = right[r_idx][0]**2 + right[r_idx][1]**2           
            if l_dist < r_dist:
                to_return_points.append(left[l_idx])
                l_idx+=1
            else:
                to_return_points.append(right[r_idx])
                r_idx+=1  
                
        if l_idx==len(left):
            while r_idx < len(right): 
                to_return_points.append(right[r_idx])
                r_idx+=1       
        else:
            while l_idx < len(left):             
                to_return_points.append(left[l_idx])
                l_idx+=1                         
            
        return to_return_points
    
    def sortkClosest(self, points):
        if len(points)==1:
            return points
        mid = len(points)//2
        left= self.sortkClosest(points[:mid])
        right = self.sortkClosest(points[mid:])
        return self.sortArray(left, right)
        
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if len(points)==1:
             return points[0]
        points = self.sortkClosest(points)
        return points[:K]     
```

(5%)

```python
class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
```