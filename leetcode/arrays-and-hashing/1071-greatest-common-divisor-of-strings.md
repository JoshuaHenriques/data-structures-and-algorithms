# 1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

*Example 1:*

```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

*Example 2:*

```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

*Example 3:*

```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

*Constraints:*
* 1 <= str1.length, str2.length <= 1000
* str1 and str2 consist of English uppercase letters.

## Solution

### Approach
We know that the GCD will be less than or qual to the shorter string, so we can iteratively calculate the prefixes and determine if it is a valid GCD. Determine the long and short strings. Iterate through the small string and append the character to currStr. Check if currStr is a valid division for both long and short strings. This is done by checking if repeating currStr the required number of times results in the original strings. If both are true then update the result.

### Complexity
$$Time: O(len(min(str1, str2)) * len(max(str1, str2)))$$

$$Space: O(len(min(str1, str2)))$$

### Code
```py
def gcdOfStrings(self, str1: str, str2: str) -> str:
    shortStr = min(str1, str2)
    longStr = max(str1, str2)

    res = ""
    currStr = ""
    for c in shortStr:
        currStr += c

        times = len(longStr) // len(currStr)
        gcdLong = currStr * times == longStr

        times = len(shortStr) // len(currStr)
        gcdShort = currStr * times == shortStr

        if gcdLong and gcdShort:
            res = currStr

    return res
```
