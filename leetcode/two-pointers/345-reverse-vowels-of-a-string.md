# 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

*Example 1:*

```
Input: s = "hello"
Output: "holle"
```

*Example 2:*

```
Input: s = "leetcode"
Output: "leotcede"
```

*Constraints:*
* 1 <= s.length <= 3 * 105
* s consist of printable ASCII characters.

## Solution 1

### Approach
First passthrough of array pushes vowels on the stack. Second passthrough replaces current value with popped vowel.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    stack = []
    s = list(s)

    for i in range(len(s)):
        if s[i] in vowels:
            stack.append(s[i])

    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = stack.pop()
            
    return "".join(s)
```

## Solution 2

### Approach
Use two pointers on each side of the string and iterate until both pointers are on a vowel and then swap the vowels.

### Complexity
$$Time: O(n)$$

$$Space: O(n)$$

### Code
```py
def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and s[i] not in vowels:
            i += 1
        while i < j and s[j] not in vowels:
            j -= 1

        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
            
    return "".join(s)
```
