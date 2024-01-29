# 1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

*Example 1:*

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

*Example 2:*

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

*Example 3:*

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

*Constraints:*
* 1 <= s.length <= 105
* s consists of lowercase English letters.
* 1 <= k <= s.length

## Naive Solution

### Approach
Using two pointers starting from 0 to k as j. We loop through that current window to count the vowels then increment the pointers.

### Complexity
$$Time: O(nk)$$

$$Space: O(1)$$

### Code
```py
def maxVowels(self, s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    i, j = 0, k
    currCnt, cnt = 0, 0

    while j <= len(s):
        for c in s[i:j]:
            if c in vowels:
                currCnt += 1
        cnt = max(cnt, currCnt)
        currCnt = 0
        i += 1
        j += 1 

    return cnt
```

## Optimized Solution

### Approach
With some preproccessing, count the vowels in the current window. Then when incrementing the pointers we adjust the count if we removed a vowel and/or adding a vowel.

### Complexity
$$Time: O(n-k)$$

$$Space: O(1)$$

### Code
```py
def maxVowels(self, s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    i, j = 0, k - 1
    currCnt, cnt = 0, 0

    for c in s[i:j + 1]:
        if c in vowels:
            cnt += 1
            currCnt += 1
    i += 1
    j += 1

    while j < len(s):
        if s[i - 1] in vowels:
            currCnt -= 1
        if s[j] in vowels:
            currCnt += 1
        cnt = max(cnt, currCnt)
        i += 1
        j += 1

    return cnt
```
