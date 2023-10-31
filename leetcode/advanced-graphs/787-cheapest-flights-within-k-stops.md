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
Using Dijkstra's Algorithm we first create our adjacency map, initialize our array to keep track of our steps at each city and initial our meanHeap with at the beginning of src. In our while minHeap iterations first we check if we visited the current city and it had fewer steps then the current steps, if it did then we can skip it. Second we check if our current steps is greater than k. Third we return if we hit our destination. After those check we update the current city's steps in bestVisited and BFS the neighbouring cities from our adjacency map.

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
We use Bellman-Ford's Algorithm because of the "at msot k stops" part of the problem since the algorithm is efficent as finding the shorest/less weighted path to all other vertices. Initialize our prices tracking array and set the src price to 0. This tells us how much the cost is to reach that city. We use a second temporary tracker so we dont update a city's price when we shouldn't have for that step because we would end up processing a path that had an extra node on it which wouldn't satisfy the k stops part of the problem. So we iterate k+1 times and each iteration we make a copy of our prices tracker and iterate through every edge. In each iteration of that we check if the price to get to "s" is "inf", which means we can't get to src. We check if the price to get to "s" plus the current edge price is less then the price it takes to get to "d", if so we update the price to get to d. We check the tempPrices[d] since there was a chance we updated that value before. After checking all the edges for that k iteration we update the original prices array. 

### Complexity
$$Time: O(E*k)$$

$$Space: O(n)$$

### Code
```
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1):
        tempPrices = prices.copy()

        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue

            if prices[s] + p < tempPrices[d]:
                tempPrices[d] = prices[s] + p

        prices = tempPrices

    return -1 if prices[dst] == float("inf") else prices[dst]
```