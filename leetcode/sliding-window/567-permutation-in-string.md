# 567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

*Example 1:*

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

*Example 2:*

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

*Constraints:*

```
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
```

## Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(26*n)$$

$$Space: O()$$

### Code
```
def checkInclusion(self, s1: str, s2: str) -> bool:
    i, j = 0, len(s1) - 1
    # Use alphabet array for practice
    s1_hashmap = defaultdict(int)
    s2_hashmap = defaultdict(int)

    if len(s1) == 1 and s1 in s2:
        return True

    if len(s1) > len(s2):
        return False

    for char in s1:
        s1_hashmap[char] += 1

    for char in s2[i:j+1]:
        s2_hashmap[char] += 1

    while j < len(s2):
        if s1_hashmap == s2_hashmap:
            return True

        s2_hashmap[s2[i]] -= 1
        if s2_hashmap[s2[i]] == 0:
            s2_hashmap.pop(s2[i])
        i += 1
        j += 1

        if j < len(s2):
            s2_hashmap[s2[j]] += 1

    return False
```

## Optimized Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
# code
```