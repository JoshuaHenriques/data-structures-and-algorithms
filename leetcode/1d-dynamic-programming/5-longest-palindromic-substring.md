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
For each character we check if every substring with that character is a palindrome. There are a total of n^2 such substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes O(n) time, the run time complexity is O(n^3)

### Complexity
$$Time: O(n^3)$$

$$Space: O(n)$$

### Code
```
def longestPalindrome(self, s: str) -> str:
    if len(s) <= 1:
        return s
    
    Max_Len=1
    Max_Str=s[0]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                Max_Len = j-i+1
                Max_Str = s[i:j+1]

    return Max_Str
```

## Recusrive Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O(n^3)$$

$$Space: O(n)$$

### Code
```
def longestPalindrome(self, s: str) -> str:
    if s == s[::-1]:
        return s

    left = self.longestPalindrome(s[1:])
    right = self.longestPalindrome(s[:-1])

    if len(left) > len(right):
        return left
    else:
        return right 
```

## Expand Around Center Solution

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


## Dynamic Programming Solution 

### Approach
sub(i, j) = s[i] == s[j] && dp[i+1][j-1] == 1

### Complexity
$$Time: O(n^2)$$

$$Space: O(n)$$

### Code
```
def longestPalindrome(self, s: str) -> str:
    maxLen = 1
    maxI = 0
    maxJ = 1

    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True

    for i in range(len(s) - 1, -1 , -1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                dp[i][j] = True
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    maxI = i
                    maxJ = j + 1

    return s[maxI:maxJ]
```