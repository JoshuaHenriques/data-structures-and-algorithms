# 332. Reconstruct Itinerary
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

*Example 1:*

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

*Example 2:*

```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

*Constraints:*

```
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
```

## Optimized Solution

### Approach
Sort the tickets first so they're in lexical order before creating the adjacency list. Or base cases for our dfs helper function is when the length of our result is equal to the length of the tickets plus 1 because of JFK always being first. Another base case is if the vertex doesn't have any adjacent nodes. In the dfs step we create a copy of the adjacency list since we'll be modifying while looping through it. Firstly we pop it from the adjMap, so we don't use this edge again, and append it to the result and recursively call dfs with that. If it returns True then there was a path (get node that can't go anywhere else) if not we use backtrack that decision and reinsert it back and remove it from the result.

### Complexity
$$Time: O((V + E)^2)$$

$$Space: O(E)$$

### Code
```
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # Time: O(V + E)^2 -> O(E^2)
    # Space: O(E) 
    adj = defaultdict(list)

    tickets.sort() # sorts it based on the pair
    for src, dst in tickets:
        adj[src].append(dst)

    result = ["JFK"]
    def dfs(src):
        if len(result) == len(tickets) + 1:
            return True
        if src not in adj:
            return False

        temp = list(adj[src]) # since we're modifying the list
        for i, v in enumerate(temp):
            adj[src].pop(i)
            result.append(v)

            if dfs(v):
                return True

            # backtracking
            adj[src].insert(i, v)
            result.pop()

        return False

    dfs("JFK")
    return result
```