# 547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

*Example 1:*

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

*Example 2:*

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

*Constraints:*

* 1 <= n <= 200
* n == isConnected.length
* n == isConnected[i].length
* isConnected[i][j] is 1 or 0.
* isConnected[i][i] == 1
* isConnected[i][j] == isConnected[j][i]


## Naive Solution

### Approach

Loop through the nodes/cities and call the dfs function on each index. At each index we add it to the visited set then loop through the row of connected nodes/cities. If two nodes/cities are connected and haven't been visited we first add that new node/city to visited, decrement our result, and then recursively call our dfs function on that node/city. We started our result to be the total number of nodes as the total number of provinces. Each time we find a connecting node/city as we're going through each node/city we decrement from the result since when two nodes/cities are connected it combines to 1 province so we can decrement from our result.

### Complexity

$$Time: O(n^2)$$

$$Space: O(n^2)$$

### Code

```py
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    visited = set()
    res = len(isConnected)

    def dfs(i):
        nonlocal res
        visited.add(i)
        
        for j in range(len(isConnected)):
            if i == j:
                continue

            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                res -= 1
                dfs(j)

    for i in range(len(isConnected)):
        dfs(i)

    return res
```

## Optimized Solution (Union Find)

### Approach

<!-- Describe your approach to solving the problem. -->

### Complexity

$$Time: O()$$

$$Space: O()$$

### Code

```py

```
