# 973. K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

*Example 1:*

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

*Example 2:*

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

*Constraints:*

```
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
```

## Naive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(nlogn)$$

$$Space: O(n)$$

### Code
```
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    hashmap = defaultdict(list)

    for x, y in points:
        hashmap[cc].append((x, y))

    result = []

    for key in sorted(list(hashmap.keys()))[:k]:
        result.extend(hashmap[key])

    return result[:k]
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(klogn)$$

$$Space: O(n)$$

### Code
```
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    minHeap = []

    for x, y in points:
        dist = sqrt((x - 0)**2 + (y - 0)**2)
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)

    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        result.append([x, y])
        k -= 1

    return result
```