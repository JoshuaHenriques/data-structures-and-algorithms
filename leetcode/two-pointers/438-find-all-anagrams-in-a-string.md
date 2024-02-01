# 438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

*Example 1:*

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

*Example 2:*

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

*Constraints:*
* 1 <= s.length, p.length <= 3 * 104
* s and p consist of lowercase English letters.

## Naive Solution

### Approach
Check at each window size if that substring is an anagram or not, if so we append the starting index in the result.

### Complexity
$$Time: O(s*p)$$

$$Space: O(1)$$

### Code
```py
def findAnagrams(self, s: str, p: str) -> List[int]:
    i, j = 0, len(p) - 1
    res = []

    while j < len(s):
        if self.isAnagram(s[i:j + 1], p):
            res.append(i)
            i += 1
            j += 1
        else:
            i += 1
            j += 1

    return res

def isAnagram(self, s: str, p: str) -> bool:
    s = "".join(sorted(list(s)))
    p = "".join(sorted(list(p)))

    for i in range(len(p)):
        if s[i] != p[i]:
            return False

    return True
```

## Solution

### Approach
Two maps with counters, one for p and one for s. Preprocess the sMap by adding the counters to it before iterating through the s string. Each time we shift the window we adjust the counters and see if both maps equal each other, if so we have an anagram so we append the starting index to the res.

### Complexity
$$Time: O(s)$$

$$Space: O(1)$$

### Code
```py
def findAnagrams(self, s: str, p: str) -> List[int]:
    pMap = defaultdict(int)
    sMap = defaultdict(int)
    res = []

    for c in p:
        pMap[c] += 1

    i, j = 0, len(p) - 1
    for c in s[i:j + 1]:
        sMap[c] += 1
        
    while j < len(s):
        if sMap == pMap:
            res.append(i)

        sMap[s[i]] -= 1
        if sMap[s[i]] <= 0:
            del sMap[s[i]]
        i += 1
        j += 1

        if j < len(s):
            sMap[s[j]] += 1

    return res
```