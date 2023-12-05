# 207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

*Example 1:*

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

*Example 2:*

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

*Constraints:*

```
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
```

## DFS Solution

### Approach
Create an adjacency map and populate it by iterating through the prerequisites (edges). For each numCourses (vertex) in the adjacency map we call our dfs helper function. In our dfs function we first check if the graph has a cycle by seeing if we visited this vertext before, if so we return False, if not we add it to the visited set. If the vertex has no adjacent vertices then we know can complete that course or visit that node. If it has adjacent vertices then we recursively call the dfs function on each one and if it didn't return false we pop that vertex from the list and from the visited set. Return true it looped through everything.

### Complexity
$$Time: O(E + V)$$

$$Space: O(E + V)$$

### Code
```
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    if len(prerequisites) == 0:
        return True

    adjMap = defaultdict(list)
    vertices = numCourses
    edges = prerequisites
    visited = set()

    # populate adjMap
    for v1, v2 in edges:
        adjMap[v1].append(v2)
        adjMap[v2]

    def dfs(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)

        if len(adjMap[vertex]) == 0:
            return True

        for v in adjMap[vertex]:
            if not dfs(v):
                return False
        adjMap[vertex] = []
        visited.remove(v)

        return True

    for vertex in adjMap:
        if not dfs(vertex):
            return False
        visited = set()

    return True
```

### Cleaner Code
```
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjMap = defaultdict(list)
    vertices = numCourses
    edges = prerequisites

    # populate adjMap
    for v1, v2 in edges:
        adjMap[v1].append(v2)
        adjMap[v2]

    visiting = set()

    def dfs(vertex):
        if vertex in visiting:
            return False
        if adjMap[vertex] == []:
            return True
            
        visiting.add(vertex)

        for v in adjMap[vertex]:
            if not dfs(v):
                return False
        adjMap[vertex] = []
        visiting.remove(vertex)
        return True

    for vertex in range(vertices):
        if not dfs(vertex):
            return False

    return True
```