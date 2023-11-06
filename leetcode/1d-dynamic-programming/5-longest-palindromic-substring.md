# 5. Longest Palindromic Substring
Given a string s, return the longest
palindromic
substring
in s.

*Example 1:*

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

*Example 2:*

```
Input: s = "cbbd"
Output: "bb"
```

*Constraints:*

```
1 <= s.length <= 1000
s consist of only digits and English letters.
```

## Naive Solution

### Approach
For each character we check if every substring with that character is a palindrome.

### Complexity
$$Time: O(n^3)$$

$$Space: O(n)$$

## Optimized Solution

### Approach
We optimize by changing how we check if it's a palindrome, we pretend that each position we check is the middle of the palidrome and then check the left and right characters if they're equal until it's not and record the longest palindrome if it made it. If not then we start that whole process again for the next character. This optimizes the brute force O(n^3) solution to O(n^2). We check both the even and odd substrings

### Complexity
$$Time: O(n^2)$$

$$Space: O(n)$$

### Code
```
def longestPalindrome(self, s: str) -> str:
    result = ""
    resultLen = 0
    resL = 0
    resR = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resultLen:
                resL = l
                resR = r + 1
                resultLen = r - l + 1

            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resultLen:
                resL = l
                resR = r + 1
                resultLen = r - l + 1
            l -= 1
            r += 1
    
    # return result
    return s[resL:resR]
```