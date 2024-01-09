#  763. Partition Labels
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

*Example 1:*

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

*Example 2:*

```
Input: s = "eccbbbbdec"
Output: [10]
```

*Constraints:*

```
1 <= s.length <= 500
s consists of lowercase English letters.
```

## Solution 1

### Approach
Count the frequency of the characters. Create a set to keep track of the current characters. Iterate through the array, at each step we add that character to the set and subtract 1 from the freq at that character. If the freq for that character is 0 we can remove it from the tracked characters. If the current tracked characters is 0 that means we reached a point where we can make a valid partition and we add that length to the result by remembering the last parition length we made.

### Complexity
$$Time: O(n)$$

$$Space: O(26)$$

### Code
```py
def partitionLabels(self, s: str) -> List[int]:
    freq = defaultdict(int)
    res = []
    last = 0
    for c in s:
        freq[c] += 1

    currFreq = freq
    curr = set()
    for i in range(len(s)):
        curr.add(s[i])
        currFreq[s[i]] -= 1
        if currFreq[s[i]] == 0:
            curr.remove(s[i])
        
        if len(curr) == 0:
            res.append(i + 1 - last)
            last = i + 1

    return res
```

## Solution 2

### Approach
Create a hashmap that has the character is the key and the last index occurence of that character is the value. During the iteration of the string we'll keep track of the current size of the partition and the minimum end of that partition. The end will be updated anytime we see a character with a lastIndex larger than the previous one. If we can get to that end index we can successfully update our partition size.

### Complexity
$$Time: O(n)$$

$$Space: O(26)$$

### Code
```py
def partitionLabels(self, s: str) -> List[int]:
    lastIndex = {}

    for i, c in enumerate(s):
        lastIndex[c] = i

    res = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])

        if i == end:
            res.append(size)
            size = 0

    return res
```
