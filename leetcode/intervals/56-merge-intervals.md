# 56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

*Example 1:*

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

*Example 2:*

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

*Constraints:*

* 1 <= intervals.length <= 104
* intervals[i].length == 2
* 0 <= starti <= endi <= 104

## Solution 1 (Messy)

### Approach
Interate through the intervals, check if the end of the new interval is less than the start of the current interval, if so we can append to result, join both lists and return. If the start of the new interval is greater than the end of the current interval we append the current interval and continue. If there is overlapping then we merge the two intervals by getting the min of the starts and the max of the ends.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []

    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i + 1][0]:
            res.append(intervals[i])
            if i + 1 == len(intervals) - 1:
                res.append(intervals[i + 1])
        elif intervals[i][0] > intervals[i + 1][1]:
            res.append(intervals[i])
            if i + 1 == len(intervals) - 1:
                res.append(intervals[i + 1])
        else:
            newInterval = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
            if i + 1 == len(intervals) - 1:
                res.append(newInterval)
            else:
                intervals[i + 1] = newInterval

    return res if len(intervals) != 1 else intervals
```

## Solution 2 

### Approach
Same as above just cleaner code.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []

    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i + 1][0]:
            res.append(intervals[i])
            if i + 1 == len(intervals) - 1:
                res.append(intervals[i + 1])
        elif intervals[i][0] > intervals[i + 1][1]:
            res.append(intervals[i])
            if i + 1 == len(intervals) - 1:
                res.append(intervals[i + 1])
        else:
            newInterval = [min(intervals[i][0], intervals[i + 1][0]), max(intervals[i][1], intervals[i + 1][1])]
            if i + 1 == len(intervals) - 1:
                res.append(newInterval)
            else:
                intervals[i + 1] = newInterval

    return res if len(intervals) != 1 else intervals
```
