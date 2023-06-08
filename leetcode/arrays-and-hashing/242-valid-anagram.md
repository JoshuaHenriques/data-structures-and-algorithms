# Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

*Example 1:*

```
Input: s = "anagram", t = "nagaram"
Output: true
```

*Example 2:*

```
Input: s = "rat", t = "car"
Output: false
```

*Constraints:*

```
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
```

## Naive Solution

### Approach
First check if the length of both strings are the same. Use a hashmap to record the frequencies of each character in the first string. Loop through the second string and also record the frequencies of it's characters. Loop through one of the dictionaries and compare the frequencies of both dictionaries, if they are the same then it's an anagram

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_s, freq_t = {}, {}

    for i in range(len(s)):
        freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
        freq_t[t[i]] = 1 + freq_t.get(t[i], 0)

    for key in freq_s:
        if key not in freq_t:
            return False
        if freq_s[key] != freq_t[key]:
            return False
    
    return True
```

## Optimized Solution

### Approach
Sort the strings to have the same order and compare the strings

### Complexity
$$Time: O(nlogn)$$

$$Space: O(1)$$

### Code
```
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    if s != t:
        return False

    return True
```