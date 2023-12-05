# 17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

*Example 1:*

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

*Example 2:*

```
Input: digits = ""
Output: []
```

*Example 3:*

```
Input: digits = "2"
Output: ["a","b","c"]
```

*Constraints:*

```
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
```

## Solution

### Approach
Use a hashmap to map the digits to the characters. We create our dfs helper function with the parameters i, the index of the digit we're at in the string digits, and curr which is the current string we're making. Base case is when the current string we're building equals the input digits string, if so we append to our result and return. If not, we iterate through the characters that digit maps too and we recursively call dfs while incrementing i and appending that character to the current string. 

### Complexity
$$Time: O(n*4^n)$$

$$Space: O(n)$$

### Code
```
def letterCombinations(self, digits: str) -> List[str]:
    result = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(i, curr):
        if len(curr) == len(digits):
            result.append(curr)
            return

        for char in digitToChar[digits[i]]:
            dfs(i+1, curr+char)

    if digits:
        dfs(0, "")

    return result
```