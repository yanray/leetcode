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

[Approach 1] (51%) 

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthdays1 = [31, 28, 31, 30, 31, 30,  
                        31, 31, 30, 31, 30, 31 ]
        monthdays2= [31, 29, 31, 30, 31, 30,  
                        31, 31, 30, 31, 30, 31 ]
        dat1=date1.split('-')
        dat2=date2.split('-')
        year1,month1,day1=dat1[:]
        year2,month2,day2=dat2[:]
        def count(year,month,day):
            n=0
            for i in range(1970,year):
                if leap(i):
                    n+=366
                else:
                    n+=365
            n+=day
            if leap(year):
                for i in range(0,month-1):
                    n+=monthdays2[i]
            else:
                for i in range(0,month-1):
                    n+=monthdays1[i]       
            return n
        def leap(year):
            if (year%4)==0:
                if (year%100==0):
                    if (year%400==0):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        y1=count(int(year1),int(month1),int(day1))
        y2=count(int(year2),int(month2),int(day2))
        return abs(y2-y1)
```

[Approach 2: Using datetime] (99%)

```python
from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = list(map(int, date1.split('-')))
        date2 = list(map(int, date2.split('-')))
        
        one = date(date1[0], date1[1], date1[2])
        two =  date(date2[0], date2[1], date2[2])
        delta = one - two
        
        return(abs(delta.days))
```

```python
from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        get_date = lambda x: date(*map(int,x.split('-')))
        return abs((get_date(date1)-get_date(date2)).days)
```

```python
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        return abs(int((datetime.datetime(y1,m1,d1)- datetime.datetime(y2,m2,d2)).days))
```