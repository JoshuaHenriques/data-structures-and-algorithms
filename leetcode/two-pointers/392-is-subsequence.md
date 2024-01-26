# 392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

*Example 1:*

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

*Example 2:*

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

*Constraints:*
* 0 <= s.length <= 100
* 0 <= t.length <= 104
* s and t consist only of lowercase English letters.

## Solution

### Approach
Use two pointers for both strings. If they are the same character then iterate both pointers, if not we just iterate the j pointer. When we hit the end of the while loop, we can return the boolean if the i pointer reached the end of the first string. If it did then we successfully checked that s is a subsequence.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```py
def isSubsequence(self, s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    return i == len(s)
```
