# 567. Permutation in String (Sliding Window)
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


## Optimized Solution

### Approach
Loop through the length of s1 to get the freq of the characters and store it in the alphabet array. Loop through range 26 and increment matches if s1count and s2count are the same at that index but incrementing it would make it took large by one so we have to decrement matches if they were equal. Do the same with the left pointer but the inverse

### Complexity
$$Time: O(26*n)$$

$$Space: O(n)$$

### Code
```
def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26
```
## Solution

### Approach
Basically the same solution as the above but the data structure is using a hashmap

### Complexity
$$Time: O(26*n)$$

$$Space: O(n)$$

### Code
```
def checkInclusion(self, s1: str, s2: str) -> bool:
    i, j = 0, len(s1) - 1`
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