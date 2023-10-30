# 787. Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

*Example 1:*

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

*Example 2:*

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

*Example 3:*

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

*Constraints:*

```
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
```

## Dijkstra's Algorithm Solution

### Approach
Double 

### Complexity
$$Time: O(n * len(flights) * log(n))$$

$$Space: O(n)$$

### Code
```
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adjMap = defaultdict(list)

    for s, d, price in flights:
        adjMap[s].append((price, d))

    # initialized to maximum
    bestVisited = [2**31]*n 

    # start from beginning, [(price, steps, city)]
    minHeap = [(0, -1, src)] 

    while minHeap:
        price, steps, city = heapq.heappop(minHeap)
        # city has been visited and the current steps are more than last time
        if bestVisited[city] <= steps: 
            continue

        # curr steps is more than k
        if steps > k:
            continue

        # reached the destination
        if city == dst:
            return price

        # update steps
        bestVisited[city] = steps
        for neighPrice, neigh in adjMap[city]:
            heapq.heappush(minHeap, (price + neighPrice, steps + 1, neigh))

    return -1
```

## Bellman-Ford Algorithm Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```