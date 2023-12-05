# 207. Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

*Example 1:*

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

*Example 2:*

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

*Example 3:*

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

*Constraints:*

```
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
```

## DFS Solution

### Approach
Simillar to the Course Schedule II solution. To solve this question we use topological sort to get the linear ordering of vertices. Create an adjacency map and populate it by iterating through the prerequisites (edges). For each numCourses (vertex) in the adjacency map we call our dfs helper function. In our dfs function we first check if the graph has a cycle by checking if the vertex is already in our cycle set, if so we return False, if not we add it to the visited set. We then check if we visited this vertex before in a different set, if so we just return True. Then we add the current vertex to the cycle set and if it has adjacent vertices then we recursively call the dfs function on each one and if it didn't return false we remove it from the cycle set since we're no longer on the path that we're looking at. Then we can add it to the visited set since we looked through all it's adjacent vertices and now we can add it to our output.  Return true if it looped through everything.

### Complexity
$$Time: O(E + V)$$

$$Space: O(E + V)$$

### Code
```
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        vertices = numCourses
        edges = prerequisites

        # populate adjMap
        for v1, v2 in edges:
            adjMap[v1].append(v2)
            adjMap[v2]

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visited, cycle = set(), set()

        def dfs(vertex):
            if vertex in cycle:
                return False
            if vertex in visited:
                return True

            cycle.add(vertex)
            for v in adjMap[vertex]:
                if not dfs(v):
                    return False
            
            cycle.remove(vertex)
            visited.add(vertex)
            output.append(vertex)

            return True

        for vertex in range(vertices):
            if not dfs(vertex):
                return []
        return output
```