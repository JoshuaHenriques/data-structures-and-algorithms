# 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

*Example 1:*

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

*Example 2:*

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

*Example 3:*

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

*Constraints:*

```
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```

## Solution 1

### Approach
Using the sliding window algorithm create two pointers, i and j, that start at index 0 and 1. Pass through the array and check if the character at j is in the substring before it, if it isn't then increment j to increase the window while adding to the longest substring counter and assigning it to max_longest if its the new max, if it is then reset the longest substring counter back to 1 and slide the window over by incrementing i and reassign j to i + 1.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        max_longest = 1
        longest = 1

        if len(s) == 0:
            return 0

        while j < len(s):
            if s[j] in s[i:j]:
                longest = 1
                i += 1
                j = i + 1
            else:
                longest += 1
                j += 1

            max_longest = max(max_longest, longest)
        return max_longest
```