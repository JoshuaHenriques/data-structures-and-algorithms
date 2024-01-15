# 435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

*Example 1:*

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

*Example 2:*

```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

*Example 3:*

```
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

*Constraints:*

* 1 <= intervals.length <= 105
* intervals[i].length == 2
* -5 * 104 <= starti < endi <= 5 * 104

## Solution

### Approach
Don't need to create or modify the array to track the result. First sort the array to help find the overlapping intervals. Track the first interval's end (prevEnd) then iterate through the intervals starting from index 1. If the current start is bigger than the previous end it's not overlapping and we can update the prevEnd to this new end. If it is we increment our result variable and set the prevEnd to the smallest end value of the two so there is less of a chance for another interval to overlap.

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```py
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()

    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(prevEnd, end)

    return res
```
