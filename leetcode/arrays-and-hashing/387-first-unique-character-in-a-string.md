# 387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

*Example 1:*

```
Input: s = "leetcode"
Output: 0
```

*Example 2:*

```
Input: s = "loveleetcode"
Output: 2
```

*Example 3:*

```
Input: s = "aabb"
Output: -1
```

*Constraints:*

* 1 <= s.length <= 105
* s consists of only lowercase English letters.

## Solution

### Approach
Get the character frequencies of the string then iterate through the hashmap and return the index of the first value that is 1. 

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def firstUniqChar(self, s: str) -> int:
    freq = defaultdict(int)

    for c in s:
        freq[c] += 1

    for key in freq:
        if freq[key] == 1:
            return s.index(key)

    return -1
```