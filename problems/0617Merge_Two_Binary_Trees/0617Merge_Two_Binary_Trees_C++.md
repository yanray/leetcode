## Number of Days Between Two Dates

### Problem Link

https://leetcode.com/problems/binary-tree-paths/

### Problem Description 

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

```
Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

```

```
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

```

**Constraints:**

The given dates are valid dates between the years 1971 and 2100.

### Code (python)

[Approach 1: accumulate days from 1971] (100%) 

```c++
class Solution {
public:
    int daysBetweenDates(string date1, string date2) {
        return abs(daysPassedSince1971(date1) - daysPassedSince1971(date2));
    }
    bool isLeapYear(int year){
        return (year%400 == 0)||(year%100 != 0 && year%4 == 0);
    }
    int daysPassedSince1971(string date){
        int year = stoi(date.substr(0,4));
        int month = stoi(date.substr(5,2));
        int day = stoi(date.substr(8,2));
        
        vector<int> months ({0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31});
        
        for(int i=1971;i<year;i++){
            day += isLeapYear(i) ? 366 : 365;
        }
        
        for(int i=1;i<month;i++){
            if(i==2 && isLeapYear(year)){
                day += 1;
            }
            day += months[i];
        }
        
        return day;
    }
    
};
```

https://leetcode-cn.com/problems/number-of-days-between-two-dates/solution/ri-qi-zhi-jian-ge-ji-tian-by-leetcode-solution/