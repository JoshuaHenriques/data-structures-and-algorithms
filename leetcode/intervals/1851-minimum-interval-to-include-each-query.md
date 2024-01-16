# 1851. Minimum Interval to Include Each Query
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

*Example 1:*

```
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
```

*Example 2:*

```
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
```

*Constraints:*

* 1 <= intervals.length <= 105
* 1 <= queries.length <= 105
* intervals[i].length == 2
* 1 <= lefti <= righti <= 107
* 1 <= queries[j] <= 107

## Naive Solution (TLE)

### Approach
Gather the sizes of the intervals. Iterate through the queries

### Complexity
$$Time: O(n*q)$$

$$Space: O(n)$$

### Code
```py
def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    ranges = [-1 for _ in intervals]
    res = []

    for i in range(len(intervals)):
        ranges[i] = intervals[i][1] - intervals[i][0]

    for i in range(len(queries)):
        lowestR = (0, float("inf"))
        for j in range(len(intervals)):
            if queries[i] in range(intervals[j][0], intervals[j][1] + 1):
                if ranges[j] < lowestR[1]:
                    lowestR = (j, ranges[j])

        if lowestR == (0, float("inf")):
            res.append(-1)
        else:
            res.append(intervals[lowestR[0]][1] - intervals[lowestR[0]][0] + 1) 

    return res
```

## Solution

### Approach


### Complexity
$$Time: O(nlogn + qlogq)$$

$$Space: O(n)$$

### Code
```py
def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()

    minHeap = []
    res, i = {}, 0
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(minHeap, (r - l + 1, r))
            i += 1

        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)
        
        res[q] = minHeap[0][0] if minHeap else -1

    return [res[q] for q in queries]
```