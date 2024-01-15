# 253 Meeting Rooms II
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

*Example 1:*

```
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)
```

*Example 2:*

```
Input: intervals = [(4,9)]
Output: 1
```

*Constraints:*

* 0 <= intervals.length <= 100
* 0 <= intervals[i].start < intervals[i].end <= 1000

## Solution

### Approach
Seperate the start and end values in their own arrays. Create two pointers for each array and have two variables, count and result, to track the current count and result. While our s pointer doesn't reach the end we compare the current start value with the end value. If start is less than we increment the count and start pointer, else we do the opposite, decrement the count and increase the e pointer. Remember if the two values are the same we increment the end pointer since a meeting has to end before the other begins 

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def minMeetingRooms(self, intervals: List[Interval]) -> int:
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)

    return res
```
