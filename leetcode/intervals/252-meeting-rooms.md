# 252 Meeting Schedule
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

*Example 1:*

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict
```

*Example 2:*

```
Input: intervals = [(5,8),(9,15)]
Output: true
```


*Constraints:*

* 0 <= intervals.length <= 100
* 0 <= intervals[i].start < intervals[i].end <= 1000

## Solution

### Approach
Sort intervals and loop through the intervals from index 1. If the start of the current interval is ever less than the previous interval's end value then there is a overlap and we can return False.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    if len(intervals) == 0:
        return True

    intervals.sort(key = lambda i: i.start)

    prevEnd = intervals[0].end
    for inter in intervals[1:]:
        if inter.start < prevEnd:
            return False
        else:
            prevEnd = inter.end

    return True
```
