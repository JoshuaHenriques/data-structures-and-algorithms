# 131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

*Example 1:*

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

*Example 2:*

```
Input: s = "a"
Output: [["a"]]
```

*Constraints:*

```
1 <= s.length <= 16
s contains only lowercase English letters.
```

## Solution

### Approach
We have a dfs helper function with a parameter of the index of which character we're at. Base case is if the index, i, is out of bounds then we append the current partition to the result. Iterate through the string starting at index i and we check at each iteration if that substring, from string at i to j+1, is a palindrome. If so we append that substring to our partitions array and recursively call with the next character j+1. Then we pop that substring from our current partitions

### Complexity
$$Time: O(2^n)$$

$$Space: O(n)$$

### Code
```
def partition(self, s: str) -> List[List[str]]:
    res = []
    part = []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if self.isPali(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()

    dfs(0)
    return res

def isPali(self, s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True
```