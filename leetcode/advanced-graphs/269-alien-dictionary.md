# 269. Alien Dictionary (Premium)
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

1. You may assume all letters are in lowercase.
2. The dictionary is invalid, if string a is prefix of string b and b is appear before a.
3. If the order is invalid, return an empty string.
4.There may be multiple valid order of letters, return the smallest in normal lexicographical order.
5. The letters in one string are of the same rank by default and are sorted in Human dictionary order.


*Example 1:*

```
Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
```

*Example 2:*

```
Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"
```

## Solution

### Approach
Can't have a cycle and use topological sort to get the ordering. Post-order dfs, build the result in reverse order, which is topological sort.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def alienOrder(self, words: List[str]) -> str:
    adj = { c:set() for w in words for c in w }

    for i in range(len(words) - 1)
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        if j in range(minLen):
            if w1[j] != w2[j]:
                adj[w[j]].add(w2[j])
                break

        visited = {} # False=visited, True=In current path
        res = []

        def dfs(c):
            # can be replaced with a cycle and visit set 
            if c in visited:
                return visited[c]

            visited[c] = True

            for neigh in adj[c]:
                if dfs(neigh):
                    # cycle was found
                    return True

            # visited but not on the current path
            visited[c] = False
            res.append(c)

        # doesn't matter where you start on the graph
        for c in adj:
            if dfs(c):
                # cycle detected
                return ""

        res.reverse()
        return "".join(res)
```