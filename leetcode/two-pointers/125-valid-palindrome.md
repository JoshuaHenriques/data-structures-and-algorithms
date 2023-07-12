# 125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

*Example 1:*

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

*Example 2:*

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

*Example 3:*

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

*Constraints:*

```
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
```

## Solution

### Approach
Pass through the array using two pointers, from 0 and at the end of the string, and compare each character until i and j cross or equal each other.

### Complexity
$$Time: O(n)$$

$$Space: O(1)$$

### Code
```
# def isalphanum(self, c):
#     return (ord('A') <= ord(c) <= ord('Z') or
#     ord('a') <= ord(c) <= ord('z') or
#     ord('0') <= ord(c) <= ord('9'))

def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1

    while (i <= j):
        while i < j and not s[i].isalnum():
            i += 1

        while j > i and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True
```

## Solution 2

### Approach
Build a new string by removing all non-alphanumeric characters and converting to lower case then compare the new string to the reversed new string.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```
def isPalindrome2(self, s: str) -> bool:
    string = ""
    
    for char in s:
        if char.isalnum():
            string += char.lower()

    return string == string[::-1]
```