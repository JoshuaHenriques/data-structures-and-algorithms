# 647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

*Example 1:*

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

*Example 2:*

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

*Constraints:*

```
1 <= s.length <= 1000
s consists of lowercase English letters.
```

## Expand Around Center Solution

### Approach
Similar to 5. Longest Palindromic Substring. We change how we check if it's a palindrome instead of doing it the traditional way. At each character we pretend it's the middle of the palindrome and check outwards, the left and right characters if they're equal. We add to the result and keep checking until we're out of bounds or they're not equal. We have to check both even and odd sized palindromes.

### Complexity
$$Time: O(n^2)$$

$$Space: O(1)$$

### Code
```
def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1

                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                
                l -= 1
                r += 1
        
        return result
```

## 2D Dynamic Programming Solution 

### Approach
sub(i, j) = s[i] == s[j] && dp[i+1][j-1] == 1

### Complexity
$$Time: O(n^2)$$

$$Space: O(n)$$

### Code
```
def countSubstrings(self, s: str) -> int:
    result = 0

    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        result += 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                dp[i][j] = True
                result += 1

    return result
```