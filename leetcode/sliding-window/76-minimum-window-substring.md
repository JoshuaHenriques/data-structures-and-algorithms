# 76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

*Example 1:*

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

*Example 2:*

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

*Example 3:*

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

*Constraints:*

```
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
```

## Solution

### Approach
Create two hashmaps, one will have the frequency of the characters and the second would be the frequency of characters of our window. The variables "have" and "need" will represent the characters we have and need will be the count we need. Loop through string, update window hashmap, if the char is in original hashmap and if the frequency of boths maps are equal then increment the "have" variable. While have and need are equal if our window length is less than the minimum result length then update it. In the while loop let's pop from the left pointer and update the window map if that character popped was apart of the window map decrement the need variable

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity") ## infinity for the min

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""
```