## Minimum Time Visiting All Points

### Problem Link

https://leetcode.com/problems/minimum-time-visiting-all-points/

### Problem Description 

On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

* In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
* You have to visit the points in the same order as they appear in the array.

```
Example 1:

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

```

```
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5

```

**Constraints:**

* points.length == n
* 1 <= n <= 100
* points[i].length == 2
* -1000 <= points[i][0], points[i][1] <= 1000

### Code (python)

[Approach 1] (80%) 

```c++
class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        
        int times = 0;
        for(int i = 1; i < points.size(); i++){
            int dis_x = abs(points[i][0] - points[i - 1][0]);
            int dis_y = abs(points[i][1] - points[i - 1][1]);
            
            times += min(dis_x, dis_y) + abs(dis_x - dis_y);
        }
        
        return times;
    }
};
```