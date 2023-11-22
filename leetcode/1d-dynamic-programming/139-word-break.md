# 139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

*Example 1:*

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

*Example 2:*

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

*Example 3:*

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

*Constraints:*

```
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
```

## Top Down Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def dfs(i, j):
        if i >= len(s):
            return True
        elif j >= len(s):
            return False 
                        
        if s[i:j+1] in wordDict:
            return dfs(j + 1, j + 1) or dfs(i, j + 1)

        return dfs(i, j + 1)

    return dfs(0, 0)
```

## Memoization Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    memo = {}
    def dfs(i, j):
        if i in memo:
            return memo[i]

        if i >= len(s):
            memo[i] = True
            return True
        elif j >= len(s):
            return False 
                        
        if s[i:j+1] in wordDict:
            memo[i] = dfs(i, j + 1)
            memo[j + 1] = dfs(j + 1, j + 1)
            return memo[i] or memo[j + 1]

        memo[i] = dfs(i, j + 1)
        return memo[i]

    return dfs(0, 0)
```

## DP Solution

### Approach
<!-- Describe your approach to solving the problem. -->

### Complexity
$$Time: O()$$

$$Space: O()$$

### Code
```
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if i + len(word) <= len(s) and word == s[i:i + len(word)]:
                dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

    return dp[0]
```