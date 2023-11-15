# 91. Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

*Example 1:*

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

*Example 2:*

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

*Example 3:*

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

*Constraints:*

```
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
```

## Top Down Recursion (Time Limit Exceeded)

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def numDecodings(self, s: str) -> int:
    # dp(i) = dp(i + 1) + dp(i + 2)

    def dp(i):
        # index goes out by one so we can return 1 to add to answer
        if i == len(s):
            return 1

        # going out by two is invalid so we return 0
        if i > len(s):
            return 0

        # when we see a "0" it becomes invalid
        if s[i] == "0":
            return 0

        result = dp(i + 1)

        # if the two digit number is valid
        if 0 < int(s[i:i+2]) < 27:
            result += dp(i + 2)

        return result

    return dp(0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def numDecodings(self, s: str) -> int:
    # dp(i) = dp(i + 1) + dp(i + 2)
    memo = defaultdict(int)
    def dp(i):
        # index goes out by one so we can return 1 to add to answer
        if i == len(s):
            return 1

        # going out by two is invalid so we return 0
        if i > len(s):
            return 0

        # when we see a "0" it becomes invalid
        if s[i] == "0":
            return 0

        if i + 1 not in memo:
            memo[i + 1] = dp(i + 1)

        result = memo[i + 1]

        # if the two digit number is valid
        if 0 < int(s[i:i+2]) < 27:
            if i + 2 not in memo:
                memo[i + 2] = dp(i + 2)
            result += memo[i + 2]

        return result

    return dp(0)
```

## DP Solution

### Approach 

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def numDecodings(self, s: str) -> int:
    # dp(i) = dp(i + 1) + dp(i + 2)

    dp = defaultdict(int)

    for i in range(len(s), -1, -1):
        if i == len(s):
            dp[i] = 1
            continue
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            dp[i] += dp[i + 2]

    return dp[0]   
```

### Progress Code
```
 # dp(i) = dp(i + 1) + dp(i + 2)

        

        # Memoization
        # memo = defaultdict(int)
        # def dp(i):
        #     # index goes out by one so we can return 1 to add to answer
        #     if i == len(s):
        #         return 1

        #     # going out by two is invalid so we return 0
        #     if i > len(s):
        #         return 0

        #     # when we see a "0" it becomes invalid
        #     if s[i] == "0":
        #         return 0

        #     if i + 1 not in memo:
        #         memo[i + 1] = dp(i + 1)

        #     result = memo[i + 1]

        #     # if the two digit number is valid
        #     if 0 < int(s[i:i+2]) < 27:
        #         if i + 2 not in memo:
        #             memo[i + 2] = dp(i + 2)
        #         result += memo[i + 2]

        #     return result

        # return dp(0)

        # Top Down Recursion (Time Limit Exceeded)
        # def dp(i):
        #     # index goes out by one so we can return 1 to add to answer
        #     if i == len(s):
        #         return 1

        #     # going out by two is invalid so we return 0
        #     if i > len(s):
        #         return 0

        #     # when we see a "0" it becomes invalid
        #     if s[i] == "0":
        #         return 0

        #     result = dp(i + 1)

        #     # if the two digit number is valid
        #     if 0 < int(s[i:i+2]) < 27:
        #         result += dp(i + 2)

        #     return result

        # return dp(0)

        # visited = set()
        # def dp(i):
        #     if i >= len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i-1 >= 0 and i+1 < len(s) and s[i-1:i+1][0] == "0":
        #         return 0

            # print(s[i-1:i+1])
            # can't be greater than 26
            # if i >= 1 and int(s[i-1:i+1]) > 26:
            #     return 0

            # if s[i-1:i+1] in visited:
            #     return 0

            # visited.add(s[i-1:i+1])

            # have all these conditionals check first before calling these
            # so we wouldn't call dp(i+1) if it's greater than 26
            # first digit is valid when its 1 then second digit is valid from 0-9
            # first digit is valid when its 2 then second digit is valid from 0-6

            # add one to the global variable instead of returning it and adding 1
            # or return 1 when we're at the end and everything is valid?
            
            # return dp(i+1) + dp(i+2)
            # dp(0) = 1 + dp(1) + dp(2)
            # dp(1) = 1 + dp(2) + dp(3)
            # dp(2) = 1 + dp(3) + dp(4)
            # dp(3) = 0
            # dp(4) = 0


        # return dp(0)
        # return dp(0) + dp(1) ??

        # def dp(string):
        #     if string[0] == "0":
        #         return 0
        #     elif len(string) > 0 and len(string) <= 3:
        #         if len(string) == 3:
        #             if int(string[1:]) > 26:
        #                 return 2
        #         elif len(string) == 2:
        #             if int(string) > 26:
        #                 return 1
                
        #         if string[len(string) - 1] == "0":
        #             return len(string) - 1

        #         return len(string)
            
        #     return dp(string[0:1]) + dp(string[:2]) + dp(string[1:])
            
        # return dp(s)
```